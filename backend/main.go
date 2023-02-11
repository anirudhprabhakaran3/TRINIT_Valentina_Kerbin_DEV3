package main

import (
	"log"

	"github.com/anirudhprabhakaran3/TRINIT_Valentina_Kerbin_DEV3/backend/controllers"
	"github.com/anirudhprabhakaran3/TRINIT_Valentina_Kerbin_DEV3/backend/middleware"
	"github.com/anirudhprabhakaran3/TRINIT_Valentina_Kerbin_DEV3/backend/models"
	"github.com/gin-gonic/gin"
)

func main() {

	models.ConnectDatabase()

	r := gin.Default()

	r.GET("/ping", func(c *gin.Context) {
		c.String(200, "Welcome to Go and Gin!")
	})

	r.POST("/login", controllers.Login)
	r.POST("/register", controllers.Register)

	r.Use(middleware.VerifyToken)
	r.GET("/profile", controllers.GetUserInfo)

	if err := r.Run("localhost:8000"); err != nil {
		log.Fatal(err)
	}
}
