pub fn series(digits: &str, len: usize) -> Vec<String> {
    if digits.len() < len {
        return vec![];
    }
    let mut v = Vec::<String>::new();
    let end = digits.len() - len + 1;
    for i in 0..end {
        v.push(digits[i..(i + len)].to_string());
    }
    v
}
