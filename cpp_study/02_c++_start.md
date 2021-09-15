## c++의 시작

```cpp
// my first cpp

#include <iostream> // 전처리 지시자
int main() {
	using namespace std;
	cout << "welcome to the c++ world";
	cout << endl;
	cout << "you'll never regret of this" << endl;
	return 0;
}
```

### c++ 전처리기와 iostream 파일

- c++의 일반적인 입출력 기능을 사용하려면 아래 두 가지 행을 반드시 넣어야 함

```cpp
#include <iostream>
using namespace std;
// cout과 cin을 사용하려면 iostream 파일을 포함시켜야 한다.
```

### 이름 공간

- iostream을 사용할 때, 프로그램이 iostream의 정의를 사용할 수 있게 하려면 다음과 같은 이름 공간 지시자를 사용해야 한다.

```cpp
using namespace std; // using 지시자
```

- c++의 컴파일러의 표준 구성 용소인 클래스, 함수, 변수는 std라는 이름 공간 안에 담겨진다.
→ iostream 헤더 파일 안에 정의되어 있는 cout 변수가 실제로는 std::cout으로 호출
- using 지시자를 사용하면 std:: 접두어를 붙이지 않고도 std 이름 공간에 정의되어 있는 이름들을 사용할 수 있다.
- using 선언이라는 것을 사용하여 자신에게 필요한 이름들만 선택해서 사용할 수 있게 하기도 한다.

```cpp
using std::cout; // cout을 사용할 수 있게 만든다.
using std::endl; // endl을 사용할 수 있게 만든다.
using std::cin; // cin을 사용할 수 있게 만든다.
```

### cout을 이용한 c++ 출력

- cout

```cpp
cout << "c++의 세계로 오십시요.";
```

![Untitled](https://user-images.githubusercontent.com/47807421/133383828-b5ef9f7e-703f-4cc5-a88c-5e9aca992058.png)

- endl

```cpp
cout << endl;
cout << "\n";
```

- 새로운 행이 시작된다는 중요한 개념을 나타내는 특별한 c++ 표기

---

## c++ 구문

```cpp
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
```

---

## c++의 기타 구문

```cpp
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
```

---

## 함수

```cpp
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
```

```cpp
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
```

```cpp
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
```

---

## EXERCISE

1. C++ 프로그램을 구성하는 모듈
함수
2. #include <iostream> 전처리 지시자가 하는 역할
컴파일하기 전 iostream 파일 내용으로 대체
3. using namespace std; 구문이 하는 역할
std 이름 공간에 정의된 이름들을 프로그램이 사용할 수 있게 허용
4. "hello world" 문자열 출력 및 새 행 시작

```cpp
cout << "helloworld" << endl;
```

1. 키보드로부터 값을 입력받아 변수에 대입

```cpp
cin >> cheese;
```

1. 함수 정의에서 return이라는 키워드가 필요 없을 때는 언제인가?
함수의 리턴형이 void이면 키워드 return을 사용할 필요가 없다.
