### 배열 초기화 규칙

```cpp
int card[4] = {3,6,2,10}; // 맞다
int hand[4]; // 맞다

hand[4] = {3,1,2,4}; // 틀리다
```

### 문자열

```cpp
char dog[4] - {'b','e','a','3'}; // 문자열이 아니다
char cat[4] - {'b','e','a','/0'}; // 문자열이 맞다!
```

- 모든 문자열의 마지막 문자가 반드시 널(Null) 문자여야 한다.

### 배열에 문자열 저장

```cpp
#include <iostream>
using namespace std;

int main() {
	const int Size = 15;
	char name1[Size];
	char name2[Size] = "C++owboy";
	cout << "my name is " << name2 << "what is your name?\n";
	cin >> name1;
	cout << "your name is " << name1 << ", first names : " << name1[0] << endl;
	name[3] = '\0';
	cout << "my first 3 name is " << name2 << endl;
	return 0;
}
```

### 문자열 입력

- cin이 문자열의 끝을 인식하는 방법이 다름

```cpp
#include <iostream>
using namespace std;

int main() {
	const int Arsize = 20;
	char name[Arsize];
	char dessert[Arsize];
	
	cout << "이름을 입력하시오: \n";
	cin >> name;
	cout << "좋아하는 디저트도 입력하시오 \n";
	cin >> dessert;
	cout << "dessert : " << dessert << "name : " << name << endl;

	return 0;
}
```

- 키보드로는 끝내기 널 문자를 입력할 수 없기 때문에, cin에게 문자열의 끝을 알려주는 다른 수단이 필요.
(빈칸, 탭, 캐리지 리턴과 같은 화이트스페이스가 있으면 그 위치에서 문자열이 끝난 것으로 간주한다.)

**→ 단어 하나씩이 아니라 전체 어구를 하나의 문자열로 입력할 필요가 있다.(행 단위의 문자열 입력)**

- getline(), get() : 행 단위로 문자열을 압력하는 클래서 멤버 함수. 전체 입력 행을 읽는다.(개행 문자가 나올때까지 읽음)

### ※ getline()을 이용한 행 단위 입력

```cpp
#include <iostream>
using namespace std;

// getline() 함수로 한 행을 읽는다.
int main() {
	const int Arsize = 20;
	char name[Arsize];
	char dessert[Arsize];
	
	cout << "이름을 입력하시오: \n";
	cin.getline(name,Arsize); // 개행 문자가 있는 곳까지 읽는다.
	cout << "좋아하는 디저트도 입력하시오 \n";
	cin.getline(dessert,Arsize);
	cout << "dessert : " << dessert << " name : " << name << endl;

	return 0;
}
```

### ※ get()을 이용한 행 단위 입력

- get 함수는 개행 문자를 읽어서 버리지 않고, 입력 큐에 그대로 남겨둔다.

```cpp
cin.get(name, ArSize);
cin.get(dessert, ArSize); // 문제 발생
```

→ 첫 번째 호출이 입력 큐에 개행 문자를 그대로 남겨두기 때문에, 두 번째 호출은 그 개행 문자를 첫 문자로 만나게 된다. 따라서 cin.get()을 사용해 개행문자를 읽도록 만들어 다음 행으로 넘어간다.

```cpp
cin.get(name, ArSize);
cin.get(); // 개행 문자를 읽는다.
cin.get(dessert, ArSize); // 문제 발생

cin.get(name, ArSize).get(); // 같은 코드, 멤버 함수들을 결합한다.

cin.getlne(name, ArSize).getline(dessert, ArSize);
```

```cpp
#include <iostream>
using namespace std;

// get() 함수로 한 행을 읽는다.
int main() {
	const int Arsize = 20;
	char name[Arsize];
	char dessert[Arsize];
	
	cout << "이름을 입력하시오: \n";
	cin.get(name,Arsize).get(); // 개행 문자가 있는 곳까지 읽는다.
	cout << "좋아하는 디저트도 입력하시오 \n";
	cin.getline(dessert,Arsize);
	cout << "dessert : " << dessert << " | name : " << name << endl;

	return 0;
}
```

getline()은 사용하기가 좀 더 편하고, get()은 에러 체킹이 좀 더 쉽다~!!

### 문자열과 수치의 혼합 입력

```cpp
#include <iostream>
using namespace std;

// 수치 입력 되에 오는 문자열 입력
int main() {
	cout << "지금 사시는 아파트에 언제 입주하셨습니다?\n";
	int year;
	cin >> year;
	cout << "사시는 도시를 말씀해주시겠습니까?\n";
	char address[80];
	cin.getline(address,80);
	cout << "아파트 입주 연도 : " << year << endl;
	cout << "도시 : " << address << endl;
	return 0;
}
```

- cin이 입주 연도를 읽어들이고, Enter키가 만들어내는 개행문자를 입력 큐에 남겨두기 때문에 발생하는 문제.
- cin.getline()은 입력 큐에 남겨진 개행 문자를 빈 행으로 읽어들이고, address 배열에 널 문자열을 대입한다.

→ 이를 해결하기 위해서는 주소를 읽기 전에 개행 문자를 읽어 허공에다 버려야 한다.
→ 매개변수를 사용하지 않는 get()이나, 하나의 char형 배개변수를 사용하는 get()을 호출하는 것을 포함하여, 여러 가지 방법으로 해결이 가능하다.

```cpp
cin >> year;
cin.get(); // 또는 cin.get(ch);

(cin >> year).get(); // 같은 코드
```

```cpp
#include <iostream>
using namespace std;

// 수치 입력 되에 오는 문자열 입력
int main() {
	cout << "지금 사시는 아파트에 언제 입주하셨습니까?\n";
	int year;
	(cin >> year).get();
	cout << "사시는 도시를 말씀해주시겠습니까?\n";
	char address[80];
	cin.getline(address,80);
	cout << "아파트 입주 연도 : " << year << endl;
	cout << "도시 : " << address << endl;
	return 0;
}
```

---

## String 클래스

- 문자열을 저장하는데 문자 배열 사용 대신, string형 변수(객체)를 사용할 수 있다.
- string 클래스를 사용하려면 string 헤더 파일을 포함시켜야 한다.

```cpp
#include <iostream>
#include <string> // string 클래스 사용
using namespace std;

// C++ string 클래스를 사용
int main() {
	char charrl1[20];			// 빈 배열
	char charrl2[20] = "jaguar"; // 초기화 배열
	string str1;				// 빈 string 객체
	string str2 = "panther";	// 초기화 string 객체

	cout << "고양이과 동물 한 종을 입력하시오: ";
	cin >> charrl1;
	cout << "고양이과 다른 동물 한 종을 입력하시오: ";
	cin >> str1;
	cout << charrl1 << " " << charrl2 << " " << str1 << " " << str1 << endl;
	return 0;
}
```

- string 객체와 문자 배열의 가장 큰 차이점은 string 객체를 배열이 아니라 단순 변수로 선언하는 것.
- str1 선언은 길이가 0인 string 객체를 생성. 따라서 배열을 사용하는 것보다 편리하고 안전하다.

### string 클래서의 조작

- cstring 헤더 파일에 있는 함수들 사용 가능

```cpp
strcpy(charr1, charr2); // charr2를 charr1에 복사한다
strcat(charr1, charr2); // charr2를 charr1에 추가한다.
```

```cpp
#include <iostream>
#include <string>
#include <cstring> // c스타일 문자열 라이브러리

using namespace std;

// C++ string 클래스를 사용
int main() {
	char charr1[20];			
	char charr2[20] = "jaguar"; 
	string str1;				
	string str2 = "panther";

	// string 객체의 대입과 문자 배열의 대입
	str1=str2;				//str2를 str1에 복사
	strcpy(charr1,charr2);//charrl2를 charrl1에 복사

	// string 객체의 추가와 문자 배열의 추가
	str1 += " paste";		//strl 끝에 paste 추가
	strcat(charr1," juice");//charrl1 끝에 juice 추가

	// string 객체의 길이 구하기위 C 스타일 문자열의 길이 구하기
	int len1 = str1.size();   //str1의 길이를 구한다
	int len2 = strlen(charr1);//charr1의 길이를 구한다.

	cout << str1 << " 문자열에는 " << len1 << "개의 문자가 들어있다.\n";
	cout << charr1 << " 문자열에는 " << len2 << "개의 문자가 들어있다.\n";
	return 0;
}
```

- string 객체 조작을 라이브러리 함수로 구현하면 좀 더 간단하다.

```cpp
str3 = str1 + str2;
//을 밑의 함수로도 구현이 가능하다.
strcpy(charr3,charr1);
strcat(charr3,charr2);
```

## ※ 구조체

- 구조체(사용자가 정의할 수 있는 데이터형)는 개체 지향 프로그래밍의 핵심인 클래스의 기초가 된다.
1. 구조체 서술 정의 : 구조체 안에 저장할 여러 가지 데이터형들을 서술하고 이름을 정한다.
2. 구조체 서술에 따라 구조체 변수 생성 : 구조체 데이터 객체를 생성하는 단계

```cpp
// 3개의 멤버를 가진 inflatable 형 구조체
struct inflatable // 구조체 선언
{
	char name[20];
	float volume;
	double price;
};
```

- inflatable : 태그라고도 불리며 새로 만들어지는 데이터형의 이름으로 사용.

```cpp
#include <iostream>
using namespace std;

// 구조체 알고리즘
struct inflatable // 구조체 선언
{
	char name[20];
	float volume;
	double price;
};
int main() {
	// guest는 inflatable형의 구조체 변수이다.
	inflatable guest = 
	{
		"Glorious Gloria",  // name 값
		1.88,				// volume 값 
		29.99				// price 값
	};					

	inflatable pal = 
	{
		"Audacious Arthur",
		3.12,
		32.99
	};
	cout << "지금 판매하고 있는 모형풍선은 \n" << guest.name << "와" << pal.name << "입니다.\n";
	cout << "두 제품을 $" << guest.price + pal.price << "에 드리겠습니다\n";
	return 0;
}
```

### C++11의 구조체 초기화

```cpp
inflatable duck {"Daphne", 0.12, 9.98}; // C++에서는 =을 생략할 수 있다.
```

### 구조체의 배열

```cpp
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
```
