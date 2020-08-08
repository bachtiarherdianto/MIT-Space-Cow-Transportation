#include <iostream>
#include <fstream>
#include <string>
#include "msc.h"


int main()
{
    std::fstream data;
    msc::checkDatabase(data);    // check database existence

    int option = msc::getOption();
    int is_continue;
    enum choice{CREATE = 1, READ, UPDATE, DELETE, FINISH};
    while (option != FINISH)
    {
        switch (option)
        {
        case CREATE:
            std::cout << "Adds information to the database"  << std::endl;
            msc::addDataCollege(data);
            break;
        case READ:
            std::cout << "Show the database"                  << std::endl;
            msc::displayDataCollege(data);
            break;
        case UPDATE:
            std::cout << "Modify the database"                << std::endl;
            msc::displayDataCollege(data);
            msc::updateRecord(data);
            msc::displayDataCollege(data);
            break;
        case DELETE:
            std::cout << "Delete information in the database" << std::endl;
            msc::displayDataCollege(data);
            msc::deleteRecord(data);
            msc::displayDataCollege(data);
            break;
        default:
            std::cout << "Error input: please input again"    << std::endl;
            break;
        }
        label_continue:
        std::cout << "[1 = continue | 0 = close]: ";
        std::cin >> is_continue;
        
        while (std::cin.fail())         // verify input
        {
            system("cls");
            std::cin.clear();
            std::cin.ignore(1000, '\n');
            std::cout << "Error input: please input again" << std::endl;
            std::cout << "[1 = continue | 0 = close]: ";
            std::cin >> is_continue;
        }
        
        if (is_continue == 1)
        {
            system("cls");
            option = msc::getOption();
        }
        else if (is_continue == 0)
        {
            break;
        }
        else
        {
            goto label_continue;
        }
    }
    std::cout << "Close program" << std::endl;
    std::cin.get();
    return 0;
}