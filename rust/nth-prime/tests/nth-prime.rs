use nth_prime as np;

#[test]
fn first_prime() {
    assert_eq!(np::nth(0), 2);
}

#[test]
fn second_prime() {
    assert_eq!(np::nth(1), 3);
}

#[test]
fn sixth_prime() {
    assert_eq!(np::nth(5), 13);
}

#[test]
fn big_prime() {
    assert_eq!(np::nth(10_000), 104_743);
}
