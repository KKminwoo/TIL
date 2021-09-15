## 포인터와 메모리 해제

- 포인터는 값 자체가 아니라 값의 주소를 저장하는 변수
- 주소 연산자(&)를 변수 앖에 붙이면 그 변수의 주소를 알아낼 수 있다.

```cpp
#include <iostream>
using namespace std;

// & 연산자로 주소를 알아낸다
int main()
{
	int donuts = 6;
	double cups = 4.5;
	cout << "donuts 값 : " << donuts;
	cout << " donuts 주소 값 : " << &donuts << endl;
	cout << "cups 값 : " << cups;
	cout << " cups 주소 값 : " << &cups << endl;
	return 0;
}
```

### 포인터 선언과 초기화(확실하게 숙지할 것!)

```cpp
#include <iostream>
using namespace std;

// 포인터 초기화
int main()
{
	int higgens = 5;
	int * pt = &higgens;

	cout << "higgens의 값 = " << higgens << ", 주소 : " << &higgens << endl;
	cout << "* pt의 값 = " << *pt << ", pt의 값 = " << pt << endl;
	return 0;
}
```

- *pt가 아니라 pt에 higgnes의 주소가 초기화되었음을 알 수 있다.

### new를 사용한 메모리 대입

- 포인터는 이름에 의해 직접 접근할 수 있는 메모리를 위한 대용 이름을 단순히 제공한다.
- **new 연산자를 사용하여 프로그램을 실행하는 동안 이름이 없는(unnamed) 메모리를 대입하는 것이 포인터의 진정한 가치!**
- 어떤 데이터형의 메모리를 원하는지 new 연산자에게 알려 주면, new 연산자는 그에 알맞은 크기의 메모리 블록을 찾아내고, 그 블록의 주소를 리턴한다.

```cpp
// pn이 데이터 객체(thing)를 지시한다.
int * pn = new int;

int higgens;
int * pt = &higgnes;

// 두 방식 모두 int 형의 주소가 포인터(pn과 pt)에 대입된다.
```

→ int형 데이터를 저장할 새로운 메모리가 필요하다고 프로그램에 알림.

단일 데이터 객체를 저장하기 위해 메모리를 확보하고, 그 주소를 포인터에 대입하는 일반적인 형식은 다음과 같다.
*typeName * pointer_name = new typeName;*
