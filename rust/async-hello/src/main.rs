use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};
use std::thread::sleep;
use std::time::Duration;

struct ReadFileFuture {}

impl Future for ReadFileFuture {
    type Output = String;

    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) ->
      Poll<Self::Output> {
        println!("Tokio! Stop polling me");
        cx.waker().wake_by_ref();
        Poll::Ready(String::from("Hello, there from file 1"))
    }
}

#[tokio::main]
async fn main() {
    println!("Hello before reading file!");

    let h1 = tokio::spawn(async {
        let future1 = ReadFileFuture {};
        println!("{:?}", future1.await);
    });

    let h2 = tokio::spawn(async {
        let file2_contents = read_from_file2().await;
        println!("{:?}", file2_contents);
    });

    let _= tokio::join!(h1, h2);
}

// 파일 읽기를 시뮬레이션 하는 함수
fn read_from_file2() -> impl Future<Output=String> {
    async {
        sleep(Duration::new(2, 0));
        String::from("Hello, there from file 2")
    }
}
