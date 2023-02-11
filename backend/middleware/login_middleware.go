package middleware

import (
	"net/http"
	"strings"

	"github.com/anirudhprabhakaran3/TRINIT_Valentina_Kerbin_DEV3/backend/services"
	"github.com/gin-gonic/gin"
)

func getToken(c *gin.Context) (string, bool) {
	authValue := c.GetHeader("Authorization")

	arr := strings.Split(authValue, " ")
	if len(arr) != 2 {
		return "", false
	}

	authType := strings.Trim(arr[0], "\n\r\t")
	if strings.ToLower(authType) != strings.ToLower("Bearer") {
		return "", false
	}
	return strings.Trim(arr[1], "\n\t\r"), true
}

func VerifyToken(c *gin.Context) {
	token, ok := getToken(c)
	if !ok {
		c.AbortWithStatusJSON(http.StatusUnauthorized, gin.H{})
		return
	}

	id, username, err := services.ValidateToken(token)
	if err != nil {
		c.AbortWithStatusJSON(http.StatusUnauthorized, gin.H{})
		return
	}

	c.Set("id", id)
	c.Set("username", username)

	c.Writer.Header().Set("Authorization", "Bearer "+token)
	c.Next()
}
