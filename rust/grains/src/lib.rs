pub fn square(s: u32) -> u64 {
    if 0 < s && s < 65 {
        2_u64.pow(s - 1)
    } else {
        panic!("Square must be between 1 and 64")
    }
}

pub fn total() -> u64 {
    (1..65).map(|n| square(n)).sum::<u64>()
}