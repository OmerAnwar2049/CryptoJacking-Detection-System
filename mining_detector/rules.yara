rule miningStrings {
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
    $str14 = "options" nocase
    $str15 = "pluginss" nocase


  condition:
     any of them
}


rule detectCrypotominingString {
  strings:
    $m1 = "merkle branch" 

  condition:
    any of them
}



rule commandLineParamsUsedForCryptomining{
  strings:
  $s1 = "--cpu-priority"
  $s2 = "-o pool"
  $s3 = "--nicehash"

  condition:
    1 of them
}
// https://github.com/bcoin-org/bcoin
// https://github.com/Neo23x0/signature-base/blob/master/yara/pua_cryptocoin_miner.yar
