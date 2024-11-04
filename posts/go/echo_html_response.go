/*
pagina web simples que pega parametro da url e injeta no html
em go usando echo framework para rodar digite o arquivo e
rode os comandos lembre de ter o go instalado

go mod init myapp
go get github.com/labstack/echo/v4@latest
go run posts/go/echo_html_response.go

acesse http://localhost:1323/seu-nome-aqui
*/

package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

func get_home(context echo.Context) error {
	name := context.Param("name")
	return context.HTML(http.StatusOK, "<h1> Hello "+name+"!<h1>")
}

func main() {
	server := echo.New()
	server.GET("/", get_home)
	server.GET("/:name", get_home)
	server.Logger.Fatal(server.Start(":1323"))
}
