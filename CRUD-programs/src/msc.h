#include <iostream>
#include <fstream>
#include <string>

namespace msc
{
    struct College
    {
        int ID;                 // primary key
        std::string Number;     // Student ID
        std::string Name;
        std::string Dept;
    };

    void writeData(std::fstream &data, int loc, College &inputStudent)
    {
        data.seekp((loc - 1) * sizeof(College), std::ios::beg);     // position seeking
        data.write(reinterpret_cast<char*> (&inputStudent), sizeof(College));
    }

    College readData(std::fstream &data, int loc)
    {
        College readStudent;
        data.seekg((loc - 1) * sizeof(College), std::ios::beg);        // position seeking (last)
        data.read(reinterpret_cast<char*> (&readStudent), sizeof(College));
        return readStudent;
    }

    int getDataSize(std::fstream &data)
    {
        int start, end;
        data.seekg(0, std::ios::beg);        // position seeking (first)
        start = data.tellg();
        data.seekg(0, std::ios::end);        // position seeking (last)
        end = data.tellg();
        return (end - start) / sizeof(College);
    }

    void displayDataCollege(std::fstream &data)
    {
        int size = getDataSize(data);

        College showStudent;
        std::cout << "No.\tID\tStudent ID\tName\tDepartment" << std::endl;
        for (int i = 1; i <= size; i++)
        {
            showStudent = readData(data, i);
            std::cout << i << "\t";
            std::cout << showStudent.ID << "\t";
            std::cout << showStudent.Number << "\t\t";
            std::cout << showStudent.Name << "\t";
            std::cout << showStudent.Dept << std::endl;
        }
    }

    void deleteRecord(std::fstream &data)
    {
        int index, size, offset;
        College blankStudent, tmpStudent;
        std::fstream tmp;

        size = getDataSize(data);

        std::cout << "Select data to delete: ";
        std::cin >> index;
        writeData(data, index, blankStudent);
        tmp.open("temp.dat", std::ios::trunc | std::ios::out | std::ios::in | std::ios::binary);

        offset = 0;
        for (int i = 1; i <= size; i++)
        {
            tmpStudent = readData(data, i);
            if (!tmpStudent.Name.empty())
            {
                writeData(tmp, i - offset, tmpStudent);
            }
            else
            {
                offset++;
                std::cout << "Deleting data" << std::endl;
            }
        }
        size = getDataSize(tmp);
        data.close();
        data.open("src.bin", std::ios::trunc | std::ios::out | std::ios::binary);
        data.close();
        data.open("src.bin", std::ios::out | std::ios::in | std::ios::binary);

        for (int i = 1; i <= size; i++)
        {
            tmpStudent = readData(tmp, i);
            writeData(data, i, tmpStudent);
        }
    }

    void updateRecord(std::fstream &data)
    {
        int index;
        College updateStudent;
        std::cout << "Select data: ";
        std::cin >> index;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

        updateStudent = readData(data, index);
        std::cout << "\n\nData details: "                   << std::endl;
        std::cout << "Student ID: " << updateStudent.Number << std::endl;
        std::cout << "Name: " << updateStudent.Name         << std::endl;
        std::cout << "Dept: " << updateStudent.Dept         << std::endl;

        std::cout << "\nModify data: "                      << std::endl;
        std::cout << "Student ID: ";
        std::getline(std::cin, updateStudent.Number);
        std::cout << "Name: ";
        std::getline(std::cin, updateStudent.Name);
        std::cout << "Dept.: ";
        std::getline(std::cin, updateStudent.Dept);

        writeData(data, index, updateStudent);
    }

    void checkDatabase(std::fstream &data)
    {
        system("cls");
        data.open("src.bin", std::ios::out | std::ios::in | std::ios::binary);
        if (data.is_open())
        {
            std::cout << "Found the database"               << std::endl;
        }
        else
        {
            std::cout << "The database is not found\n" 
                    << "Creating new database..."         << std::endl;
            data.close();
            data.open("src.bin", std::ios::trunc | std::ios::out | std::ios::in | std::ios::binary);
        }    
    }

    int getOption()
    {
        int input;
        std::cout << "\nMini Student Database Program" << std::endl;
        std::cout <<   "=============================" << std::endl;
        std::cout <<   "1| Add Student Information"    << std::endl;
        std::cout <<   "2| Show All Information"       << std::endl;
        std::cout <<   "3| Modify Student Information" << std::endl;
        std::cout <<   "4| Delete Student Information" << std::endl;
        std::cout <<   "5| Close Program"              << std::endl;
        std::cout <<   "=============================" << std::endl;
        std::cout <<   "select [1 - 5]? : ";
        std::cin >> input;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        return input;
    }

    void addDataCollege(std::fstream &data)
    {
        College inputStudent, lastStudent;

        int size = getDataSize(data);
        std::cout << "Total size: " << size << std::endl;

        if (size == 0)
        {
            inputStudent.ID = 0;        // ID start from 0
        }
        else
        {
            lastStudent = readData(data, size);
            std::cout << "Last ID: " << lastStudent.ID << std::endl;
            inputStudent.ID = lastStudent.ID + 1;
        }
        std::cout << "Name: ";
        getline(std::cin, inputStudent.Name);
        std::cout << "Dept.: ";
        getline(std::cin, inputStudent.Dept);
        std::cout << "Student ID: ";
        getline(std::cin, inputStudent.Number);
        writeData(data, size + 1, inputStudent);
    }   
}