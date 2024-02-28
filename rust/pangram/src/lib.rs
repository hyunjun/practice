//use std::collections::HashSet;
/// Determine whether a sentence is a pangram.
pub fn is_pangram(sentence: &str) -> bool {
    //let s: HashSet<char> = HashSet::from_iter(sentence.to_lowercase().chars().filter(|c| c.is_ascii() && c.is_alphabetic()).into_iter());
    //s == HashSet::from_iter("abcdefghijklmnopqrstuvwxyz".chars())
    ('a'..='z').all(|c| sentence.to_ascii_lowercase().contains(c))
}
