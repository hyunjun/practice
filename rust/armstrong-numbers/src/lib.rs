pub fn is_armstrong_number(num: u32) -> bool {
    let s = num.to_string();
    let l = s.len() as u32;
    num as u64 == s.chars().map(|c| c.to_digit(10).unwrap().pow(l) as u64).sum::<u64>()
    /*
    let mut sum: u64 = 0;
    for c in s.chars() {
        sum += c.to_digit(10).unwrap().pow(l) as u64;
    }
    num as u64 == sum
    */
}
