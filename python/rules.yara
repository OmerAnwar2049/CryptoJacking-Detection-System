rule Mining_Detected {
  strings:
    $str1 = "mine" nocase
    $str2 = "hash" nocase
    $str3 = "crypto" nocase
    $str4 = "mining" nocase
    $str5 = "cpu" nocase
    $str6 = "gpu" nocase
    $str7 = "coin" nocase
    $str8 = "pool" nocase
    $str9 = "ether" nocase
    $str10 = "blocks" nocase
    $str11 = "market" nocase
    $str12 = "payment" nocase
    $str13 = "height" nocase
    $str14 = "height" nocase

  condition:
    any of them
}


rule fun {
  strings:
    $ = "fun"

  condition:
    any of them
}
// https://github.com/bcoin-org/bcoin