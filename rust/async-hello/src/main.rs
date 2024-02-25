use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};
use std::thread::sleep;
use std::time::{Duration, Instant};

struct AsyncTimer {
    expiration_time: Instant,
}

impl Future for AsyncTimer {
    type Output = String;

    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) ->
        Poll<Self::Output> {
            if Instant::now() >= self.expiration_time {
                println!("Hello, it's time for Future 1");
                Poll::Ready(String::from("Future 1 has completed"))
            } else {
                println!("Hello, it's not yet time for Future 1. Going to sleep");
                let waker = cx.waker().clone();
                let expiration_time = self.expiration_time;
                std::thread::spawn(move || {
                    let current_time = Instant::now();
                    if current_time < expiration_time {
                        std::thread::sleep(expiration_time - current_time);
                    }
                    waker.wake();
                });
                Poll::Pending
            }
        }
}

#[tokio::main]
async fn main() {
    let h1 = tokio::spawn(async {
        let future1 = AsyncTimer {
            expiration_time: Instant::now() + Duration::from_millis(4000),
        };
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
        String::from("Future 2 has completed")
    }
}
