#include<iostream>

#include "main.hpp"

Kalkulator::Kalkulator(const int& a, const int& b) : 
   m_a(a),
   m_b(b)
{
   std::cout << "Nowy obiekt kalkulatora stworzony!" << std::endl;
   std::cout << "argument 1: " << m_a << std::endl;
   std::cout << "argument 2: " << m_b << std::endl;
}

int Kalkulator::wykonajDzialanie(const Tryb& tryb)
{
   int ret;
   std::string dzialanie;

   if(Tryb::Dodawanie == tryb)
   {
      dzialanie = "dodawanie";
      ret = m_a + m_b;
   }
   else if(Tryb::Odejmowanie == tryb)
   {
	dzialanie = " odejmowanie";
	ret= m_a-m_b;
      //TODO: dodać implementację dla pozsotałych działań
   }
	else if (Tryb::Mnozenie == tryb)
	{
		dzialanie = "mnożenie";
		ret = m_a*m_b;
	}
	else if (Tryb::Dzielenie == tryb)
	{
		dzialanie = "dzielenie";
		ret = (m_a)/(m_b);
	}

   std::cout << "Wybrane dzialanie: " << dzialanie << std::endl;

   return ret;
}

int main(int argc, char** argv)
{
   if(argc < 3)
   {
      std::cout << "Zbyt mała liczba argumentów!" << std::endl;
   }
   else
   {
      int arg1 = atoi(argv[1]);
      int arg2 = atoi(argv[2]);

      Kalkulator calc(arg1, arg2);
      int wynik = calc.wykonajDzialanie(Tryb::Dodawanie);
	int wynik1 = calc.wykonajDzialanie(Tryb::Odejmowanie);
	int wynik2 = calc.wykonajDzialanie(Tryb::Mnozenie);
	int wynik3 = calc.wykonajDzialanie(Tryb::Dzielenie);


      	std::cout << "Wynik dodawania: " << wynik << std::endl;
	std::cout << "Wynik odejmowania: " << wynik1 << std::endl;
	std::cout << "Wynik mnożenia: " << wynik2 << std::endl;
	std::cout << "Wynik dzielenie: " << wynik3 << std::endl;

      

   }

}
