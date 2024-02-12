pub fn brackets_are_balanced(string: &str) -> bool {
    const BRACKETS: &[(char, char)] = &[('(', ')'), ('[', ']'), ('{', '}')];
    let mut v: Vec<char> = Vec::new();
    for c in string.chars() {
        for b in BRACKETS.iter() {
            if c == b.1 {
                if 0 < v.len() && v.last().copied().unwrap().eq(&b.0) {
                    v.pop();
                } else {
                    v.push(c);
                }
            } else if c == b.0 {
                v.push(c);
            }
        }
    }
    v.len() == 0
}
