use std::thread;
use std::thread::sleep;
use std::time::Duration;

fn main() {
    println!("Hello before reading file!");
    let handle1 = thread::spawn(|| {
        let file1_contents = read_from_file1();
        println!("{:?}", file1_contents);
    });
    let handle2 = thread::spawn(|| {
        let file2_contents = read_from_file2();
        println!("{:?}", file2_contents);
    });
    handle1.join().unwrap();
    handle2.join().unwrap();
}
// 파일 읽기를 시뮬레이션 하는 함수
fn read_from_file1() -> String {
    sleep(Duration::new(4, 0));
    String::from("Hello, there from file 1")
}
// 파일 읽기를 시뮬레이션 하는 함수
fn read_from_file2() -> String {
    sleep(Duration::new(2, 0));
    String::from("Hello, there from file 2")
}
