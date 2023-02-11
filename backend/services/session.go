package services

import "github.com/gin-gonic/gin"

func GetSession(c *gin.Context) (uint, string, bool) {
	id, ok := c.Get("id")
	if !ok {
		return 0, "", false
	}

	username, ok := c.Get("username")
	if !ok {
		return 0, "", false
	}

	return id.(uint), username.(string), true
}
