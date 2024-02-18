pub fn raindrops(n: u32) -> String {
    /*
    let mut s = String::from("");
    if n % 3 == 0 {
        s.push_str("Pling");
    }
    if n % 5 == 0 {
        s.push_str("Plang");
    }
    if n % 7 == 0 {
        s.push_str("Plong");
    }
    */
    /*
    let s = String::from("") +
        if n % 3 == 0 { "Pling" } else { "" } +
        if n % 5 == 0 { "Plang" } else { "" } +
        if n % 7 == 0 { "Plong" } else { "" };
    */
    /*
    let mut s = String::from("");
    const NUM_STRS: &[(u32, &str)] = &[(3, "Pling"), (5, "Plang"), (7, "Plong")];
    for i in NUM_STRS.iter() {
        if n % i.0 == 0 {
            s.push_str(&i.1);
        }
    }
    */
    const NUM_STRS: &[(u32, &str)] = &[(3, "Pling"), (5, "Plang"), (7, "Plong")];
    let s = NUM_STRS.iter()
                    .map(|x| if n % x.0 == 0 { x.1 } else { "" })
                    .fold("".to_string(), |cur: String, nxt: &str| cur + nxt);
    /*
    if s.len() == 0 {
        return n.to_string();
    }
    s
    */
    /*
    if s.len() == 0 {
        n.to_string()
    } else {
        s
    }
    */
    if s.len() == 0 { n.to_string() } else { s }
}
