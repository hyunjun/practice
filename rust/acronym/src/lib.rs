pub fn abbreviate(phrase: &str) -> String {
    //  https://www.hackertouch.com/rust-split-string-on-multiple-delimiters.html
    let s = phrase.to_string();
    let v: Vec<_> = s.split([':', '-', '_', ' '].as_ref()).filter(|s| s.len() > 0).collect();
    //v.iter().map(|w| w.chars().nth(0).unwrap().to_ascii_uppercase()).into_iter().collect::<String>()
    /*
    v.iter().map(|w| {
        let uppercases = w.chars().filter(|c| c.is_ascii_uppercase());
        if uppercases.clone().count() > 0 {
            uppercases.into_iter().collect::<String>()
        } else {
            w.chars().nth(0).unwrap().to_ascii_uppercase().to_string()
        }
    }).into_iter().collect::<String>()
     */
    v.iter().map(|w| {
        w.chars().enumerate().filter(|&(i, c)| i == 0 || (w.chars().nth(i - 1).unwrap().is_ascii_uppercase() == false && c.is_ascii_uppercase())).map(|(_, c)| c).into_iter().collect::<String>().to_uppercase()
    }).into_iter().collect::<String>()
}
