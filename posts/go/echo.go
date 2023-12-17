/*
Api simples em go usando echo framework
para rodar digite o arquivo e rode os comandos

go mod init myapp
go get github.com/labstack/echo/v4
go run server.go
*/
package main
import (
    "net/http"
    "github.com/labstack/echo/v4"
)
type Messages struct {
	Message   string `json:"message"`
}

func get_home(context echo.Context) error {
    json_message := Messages{"Ola Mundo"}
    return context.JSON(http.StatusOK, json_message)
}

func main() {
    server := echo.New()
    server.GET("/", get_home)
    server.Logger.Fatal(server.Start(":1323"))
}