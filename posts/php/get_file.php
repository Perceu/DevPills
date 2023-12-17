<?php
/*
Fazendo uso do php para buscar dados remotamente
o file_get_contents aceita diversos protocolos como o get

mas e facilmente bloqueado por sistemas para requests mais completas 
pode ser usado:

 - guzzle
*/

libxml_use_internal_errors(true);

$homepage = file_get_contents('https://www.scrapethissite.com/pages/');

$doc = new DOMDocument();
$doc->loadHTML($homepage);

$xpath = new DOMXPath($doc);
$titles = $xpath->evaluate('//h3[@class="page-title"]//a');

foreach ($titles as $title) {
    echo "{$title->textContent}\n";
}