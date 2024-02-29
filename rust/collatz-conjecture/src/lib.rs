pub fn collatz_recur(count: u64, n: u64) -> Option<u64> {
    match n {
        1 => Some(count),
        _ => collatz_recur(count + 1, if n % 2 == 0 { n / 2 } else { 3 * n + 1 })
    }
}
pub fn collatz(n: u64) -> Option<u64> {
    if n < 1 {
        return None;
    }
    //collatz_recur(0, n)
    let mut num = n;
    let mut count = 0;
    while num != 1 {
        println!("{} {}", num, count);
        count += 1;
        if num % 2 == 0 {
            num = num / 2;
        } else {
            let (multiplied, is_overflowed) = num.overflowing_mul(3);
            if is_overflowed {
                return None;
            }
            let (added, is_overflowed) = multiplied.overflowing_add(1);
            if is_overflowed {
                return None;
            }
            num = added;
        }
    }
    Some(count)
}
