use std::thread::sleep;
use std::time::Duration;
use std::future::Future;

#[tokio::main]
async fn main() {
    println!("Hello before reading file!");

    let h1 = tokio::spawn(async {
        let file1_contents = read_from_file1().await;
        println!("{:?}", file1_contents);
    });

    let h2 = tokio::spawn(async {
        let file2_contents = read_from_file2().await;
        println!("{:?}", file2_contents);
    });

    let _= tokio::join!(h1, h2);
}

// 파일 읽기를 시뮬레이션 하는 함수
fn read_from_file1() -> impl Future<Output=String> {
    async {
        sleep(Duration::new(4, 0));
        println!("{:?}", "Processing file 1");
        String::from("Hello, there from file 1")
    }
}

// 파일 읽기를 시뮬레이션 하는 함수
fn read_from_file2() -> impl Future<Output=String> {
    async {
        sleep(Duration::new(2, 0));
        println!("{:?}", "Processing file 2");
        String::from("Hello, there from file 2")
    }
}
