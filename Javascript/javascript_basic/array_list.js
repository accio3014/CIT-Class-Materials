// Array
// 하나의 변수에 여러개의 값을 저장 가능, 다양한 자료형을 섞어서 저장이 가능하지만 보통의 경우 한개의 자료형으로 통일
// []기호를 사용하며, 순서의 경우 인덱스(index)라고 말하며 0으로 시작
// 값을 구분할 때는 ,를 사용하며, 길이, 크기는 몇개가 저장되어 있는지 말함
// 값을 참조 할때는
// 변수[인덱스 번호]
// 위 형식으로 참조

// var arr = [1, 2, "Hello", false];   // 가장 대표적인 방법
// let nums = new Array(1, 2, 3)       // Array 생성자를 사용해서 생성
// console.log(arr[2]);
// console.log(nums[0]);


// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ //


// Array 메소드

// length
// array.length 를 이용하여 array의 길이(몇개가 저장되어 있는지)를 리턴
// const fruits = [];
// fruits.push("banana", "apple", "peach");
// console.log(fruits.length);

// at()
// array.at(index) 은 index 번호에 해당하는 값을 리턴, index의 경우 정수가 들어감
// const array1 = [5, 12, 8, 130, 44];
// console.log(array1.at(2));

// concat()
// array1.concat(array2)
// 위 형식으로 사용하며 array1과 array2를 병합하여 새로운 array를 리턴
// const a1 = ["a", "b", "c"];
// const a2 = ["d", "e", "f"];
// const a3 = a1.concat(a2);
// console.log(a3);

