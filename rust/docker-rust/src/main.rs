use actix_web::{get, web, App, HttpResponse, HttpServer, Responder};
#[get("/")]
async fn gm() -> impl Responder {
    HttpResponse::Ok().body("Hello, Good morning!")
}
async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello there!")
}
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(gm)
            .route("/hello", web::get().to(hello))
    })
        .bind(("0.0.0.0", 8080))?
        .run()
        .await
}