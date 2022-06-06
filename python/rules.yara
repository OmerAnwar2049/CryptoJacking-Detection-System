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
    $str9 = "blocks" nocase
    $str10 = "market" nocase
    $str11 = "payment" nocase



  condition:
    any of them
}
