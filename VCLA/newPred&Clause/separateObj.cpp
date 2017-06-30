#include<fstream>
#include<iostream>
#include<string>
#include<set>
#include<cstdlib>
using namespace std;

struct Exp
{
	string text;
	string env;
	string obj;

};


int main(int argc, char* argv[])
{
	ifstream input("noAct.xml", ios::in);
	if (!input.is_open())
	{
		cout << "cannot open the file!\n";
		exit(1);
	}

	string text;
	string env;
	string obj;

	while (!input.eof())
	{
		getline(input, str);
	
		if (str.find(argv[1]) != string::npos)
		{
		  cout << str;
		  getline(input, str);
		  cout << str;
		  getline(input, str);
		  cout<<str<<"\n";
		  
		}

	}

	for (auto p = data.begin(); p != data.end(); p++)
	{
		if (p->obj == argv[1])
		{
			cout << p->text << "\n"
				<< p->env << "\n"
				<< p->obj << "\n";
		}
	}

	input.close();


}

