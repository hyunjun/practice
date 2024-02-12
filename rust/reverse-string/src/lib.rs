pub fn reverse(input: &str) -> String {
    //if input.len() == 0 {
    //    String::from("");
    //}
    /*
    let mut s = String::new();
    for i in s.len() - 1..0 {
        //s.push(input[i..i + 1].char());
        s.push(input.chars().nth(i).unwrap());
    }
    s
    */
    input.chars().rev().collect::<String>()
}
