use std::thread::sleep;
use std::time::Duration;

#[tokio::main]
async fn main() {
    println!("Hello before reading file!");

    let h1 = tokio::spawn(async {
        let file1_contents = read_from_file1();
    });

    let h2 = tokio::spawn(async {
        let file2_contents = read_from_file2();
    });

    let _= tokio::join!(h1, h2);
}

// 파일 읽기를 시뮬레이션 하는 함수
async fn read_from_file1() -> String {
    sleep(Duration::new(4, 0));
    println!("{:?}", "Processing file 1");
    String::from("Hello, there from file 1")
}

// 파일 읽기를 시뮬레이션 하는 함수
async fn read_from_file2() -> String {
    sleep(Duration::new(2, 0));
    println!("{:?}", "Processing file 2");
    String::from("Hello, there from file 2")
}
