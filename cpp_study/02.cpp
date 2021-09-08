// my first cpp

#include <iostream> // 전처리 지시자
int main() {
	using namespace std;
	cout << "welcome to the c++ world";
	cout << endl;
	cout << "you'll never regret of this" << endl;
	return 0;
}

// 변수 활용 

#include <iostream>
int main() {
	using namespace std;
	int carrots;
	carrots = 25;
	cout << "나는 당근을 ";
	cout << carrots;
	cout << "개 가지고 있다.";
	cout << endl;
	carrots = carrots - 1;
	cout << "아삭아삭, 이제 당근은 " << carrots << "개이다\n";
	return 0;
}

// cin 변수 활용 

#include <iostream>
int main() {
	using namespace std;
	int carrots;
	cout << "당근을 몇 개나 가지고 있나?" << endl;
	cin >> carrots; // c++ 입력
	cout << "여기 두 개가 더 있다\n";
	carrots = carrots + 2;
	cout << "이제 당근은 모두 " << carrots << "개이다" << endl;
	return 0;
}

// 함수 활용 

#include <iostream>
int main() {
	using namespace std;
	double area;
	cout << "마루 면적을 피트단위로 입력하시오 : ";
	cin >> area;
	double side;
	side = sqrt(area);
	cout << "사각형 마루는 한 변이 " << side << "피트 입니다." << endl;
	return 0;
}

// 함수 직접 선언하기

#include <iostream>
void simon(int n) // simon 함수 정의
{
	using namespace std;
	cout << "발가락을 " << n << "번 두드려라\n";
}
int main() {
	using namespace std;
	cout << "정수를 하나 고르시오 :";
	int count;
	cin >> count;
	simon(count);
	cout << "끝!" << endl;
	return 0;
}

// 리턴 값이 있는 사용자 정의 함수 직접 선언하기

#include <iostream>
int stonetolb(int); // 함수 원형

int main() {
	using namespace std;
	int stone;
	cout << "체중을 스톤 단위로 입력하시오 : ";
	cin >> stone;
	int pounds = stonetolb(stone);
	cout << stone << " 스톤은 " << pounds << " 파운드 입니다." << endl;
	return 0;
}
int stonetolb(int n) // simon 함수 정의
{
	return (14 * n);
}
