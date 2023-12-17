/*
Para rodar um arquivo rust faça os comandos:
cargo init
cargo run 
*/

use std::io;

fn main() {
    println!("Enter a name:");
    let mut guess = String::new();
    io::stdin().read_line(&mut guess).expect("failed to readline");
    println!("Hello, {}", guess);
}
