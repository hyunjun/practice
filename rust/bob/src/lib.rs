pub fn reply(message: &str) -> &str {
    let m = message.trim().to_string();

    let is_ending_question = m.ends_with("?");
    let is_uppercase_alphabet = m.chars().filter(|c| c.is_alphabetic()).all(|c| c.is_ascii_uppercase()) && 0 < m.chars().filter(|c| c.is_alphabetic()).count();
    if is_ending_question && is_uppercase_alphabet {
        return "Calm down, I know what I'm doing!";
    }
    if is_ending_question {
        return "Sure.";
    }
    if is_uppercase_alphabet {
        return "Whoa, chill out!";
    }

    let is_empty_or_nonalphanumeric = m.chars().filter(|c| c.is_alphanumeric()).count() == 0;
    if is_empty_or_nonalphanumeric {
        return "Fine. Be that way!";
    }
    "Whatever."
}
