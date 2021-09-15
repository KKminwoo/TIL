### char형과 int 형의 비교

```cpp
// 정수 한계값 출력
#include <iostream>
int main()
{
	using namespace std;
	char ch = 'M'; // M에 해당하는 ASCII 코드를 char형 변수 ch에 대입
	int i = ch; // 같은 코드를 int형 변수 i에 저장
	cout << ch << "의 ASCII 코드는 " << i << "입니다." << endl;

	cout << "이 문자 코드에 1을 더해보겠습니다.\n";
	ch = ch + 1;
	i = ch;
	cout << ch << "의 ASCII 코드는 " << i << "입니다.\n";

	// cout.put() 멤버 함수를 사용하여 char형 변수 ch를 출력한다.
	cout.put(ch);
	cout.put('!');
	return 0;
}
```

- cout.put('$'); = cout << "$"; → 같은 의미

### 이스케이프 시퀀스

```cpp
// 이스케이프 시퀀스 사용
#include <iostream>
int main()
{
	using namespace std;
	cout << "\a암호명 \"화려한 외출\"작전이 방금 개시되었습니다.\n";
	cout << "8자리 비밀번호를 입력하시오:________\b\b\b\b\b\b\b\b";
	long code;
	cin >> code;
	cout << "\a입력하신 비밀번호는" << code << "입니다.\n";
	return 0;
}
```

### EXERCISE

1. C++이 여러 개의 정수형을 제공하는 이유
→ 특별한 요구에 적합한 데이터형을 골라서 사용할 수 있기 때문이다. 이를 통해 메모리를 절약할 수 있고, 계산 속도가 한층 빨라질 수 있다.
