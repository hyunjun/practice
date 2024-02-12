#[derive(Debug)]
pub struct HighScores {
    scores: Vec<u32>
}

impl HighScores {
    pub fn new(scores: &[u32]) -> Self {
        HighScores { scores: scores.to_vec() }
    }

    pub fn scores(&self) -> &[u32] {
        //self.scores.try_into().unwrap_or_else(|v: Vec<u32>| panic!("Expected a Vec of length but it was {}", v.len()))
        &self.scores
    }

    pub fn latest(&self) -> Option<u32> {
        self.scores.last().copied()
    }

    pub fn personal_best(&self) -> Option<u32> {
        self.scores.iter().max().copied()
    }

    pub fn personal_top_three(&self) -> Vec<u32> {
        let l = self.scores.len();
        if l == 0 {
            return Vec::new();
        }
        let mut v = self.scores.to_vec();
        v.sort();
        v.reverse();
        let i = if l < 3 {
            l
        } else {
            3
        };
        (&v[..i]).to_vec()
    }
}
