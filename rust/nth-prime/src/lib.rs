pub fn nth_prime(n: u32) -> u32 {
    let mut primes = vec![2, 3, 5, 7];
    let mut i = 3;
    let mut num = 7;
    while i < n {
        num += 1;
        while primes.iter().any(|p| num % p == 0) {
            num += 1;
        }
        i += 1;
        primes.push(num);
    }
    num
}

pub fn nth(n: u32) -> u32 {
    match n {
        0 => 2,
        1 => 3,
        2 => 5,
        3 => 7,
        _ => nth_prime(n),
    }
}
