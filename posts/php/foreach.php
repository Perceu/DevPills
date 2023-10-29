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
 * basta acessar 0.0.0.0:8080/foreach.php
 */

$linguagens = [
    'php','python','javascript', 'html', 'css'
];

foreach ($linguagens as $linguagem) {
    print("{$linguagem}<br>");
}
