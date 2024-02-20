pub fn build_proverb(list: &[&str]) -> String {
    /*
    let mut s = String::from("");
    match list.len() {
        0 => (),
        _ => {
            let l = list.len() - 1;
            for i in 0..l {
                println!("{}\t{}", list[i], list[i + 1]);
                s.push_str(&format!("For want of a {} the {} was lost.\n", list[i], list[i + 1]).to_string());
            }
            if 0 <= l {
                s.push_str(&format!("And all for the want of a {}.", list[0]).to_string());
            }
        }
    }
    s
     */
    list.iter()
        .enumerate()
        //.filter(|&(i, _)| 0 <= i)
        .map(|(i, s)|
                if i < list.len() - 1 {
                    format!("For want of a {} the {} was lost.", s, list[i + 1])
                } else {
                    format!("And all for the want of a {}.", list[0])
                }
            )
        .collect::<Vec<_>>()
        .join("\n")
}