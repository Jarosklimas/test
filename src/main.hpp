enum class Tryb {
   Dodawanie = 1,
   Odejmowanie = 2,
   Mnozenie = 3,
   Dzielenie = 4
};

class Kalkulator{
public:   
   Kalkulator(const int& a, const int& b);
   int wykonajDzialanie(const Tryb& tryb); 

private:
   int m_a;
   int m_b;
};
