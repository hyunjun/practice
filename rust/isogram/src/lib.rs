use std::collections::HashSet;


pub fn check(candidate: &str) -> bool {
    let lowercase_str = candidate.chars().filter(|c| c.is_alphabetic()).into_iter().collect::<String>().to_lowercase();
    let s: HashSet<char> = HashSet::from_iter(lowercase_str.chars());
    lowercase_str.len() == s.len()
}
