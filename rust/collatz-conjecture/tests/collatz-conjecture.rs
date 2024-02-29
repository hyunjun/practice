use collatz_conjecture::*;

#[test]
fn one() {
    assert_eq!(Some(0), collatz(1));
}

#[test]
fn sixteen() {
    assert_eq!(Some(4), collatz(16));
}

#[test]
fn twelve() {
    assert_eq!(Some(9), collatz(12));
}

#[test]
fn one_million() {
    assert_eq!(Some(152), collatz(1_000_000));
}

#[test]
fn zero() {
    assert_eq!(None, collatz(0));
}

#[test]
fn test_110243094271() {
    let val = 110243094271;
    assert_eq!(None, collatz(val));
}

#[test]
fn max_div_3() {
    let max = u64::MAX / 3;
    assert_eq!(None, collatz(max));
}

#[test]
fn max_minus_1() {
    let max = u64::MAX - 1;
    assert_eq!(None, collatz(max));
}
