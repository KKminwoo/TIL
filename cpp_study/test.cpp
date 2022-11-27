#include <iostream>
using namespace std;

// 구조체 배열
struct inflatable
{
	char name[20];
	float volume;
	double price;
};
int main() {
	inflatable guests[2] = 
	{
		{"Bambi",0.5,21.99},	// 배열에 있는 첫 번째 구조체
		{"Godzilla",2000,565.99}// 배열에 있는 그 다음 구조체
	};					

	cout << guests[0].name << "와 " << guests[1].name << "의 부피를 합하면 " << guests[0].volume + guests[1].volume << "이다.";
	return 0;
}