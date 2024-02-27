use std::collections::HashSet;

pub fn is_anagram(word1: &str, word2: &str) -> bool {
    if word1.len() != word2.len() || word1.to_lowercase() == word2.to_lowercase() {
        return false;
    }
    let mut sorted_word1 = word1.to_lowercase().chars().collect::<Vec<_>>();
    let mut sorted_word2 = word2.to_lowercase().chars().collect::<Vec<_>>();

    sorted_word1.sort();
    sorted_word2.sort();

    sorted_word1 == sorted_word2
}

pub fn anagrams_for<'a>(word: &'a str, possible_anagrams: &'a [&str]) -> HashSet<&'a str> {
    possible_anagrams.iter().filter(|&&p| is_anagram(word, p)).cloned().collect()
}
