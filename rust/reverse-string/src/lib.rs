pub fn reverse(input: &str) -> String {
    let input_len = input.chars().count();  //  using input.len() breaks wide character case
    if input_len == 0 {
        return String::from("");
    }
    let mut s = String::new();
    for i in (0..input_len).rev() {
        //s.push(input[i..i + 1].char());
        //s.insert_str(0, &input[i..i + 1]);
        s.push(input.chars().nth(i).unwrap());
    }
    s
    //input.chars().rev().collect::<String>()
}
