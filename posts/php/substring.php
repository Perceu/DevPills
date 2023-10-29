<?php 
/*
 * Subir o servidor de desenvolvimento do PHP
 * php -S 0.0.0.0:8080
 * 
 * Tornando a pasta atual a raiz do servidor 
 * 
 * lembrando que o output do PHP se for HTML,
 * sera interpretado corretamente no navegador
 * 
 * basta acessar 0.0.0.0:8080/substring.php
 */

$linha = 'Retirando ultimo caracter de uma string x';
$nova_linha = substr($linha, 0, -1);

print("{$nova_linha}<br>");
