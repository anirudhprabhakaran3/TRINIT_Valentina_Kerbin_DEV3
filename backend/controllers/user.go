package controllers

import (
	"fmt"
	"net/http"

	"github.com/anirudhprabhakaran3/TRINIT_Valentina_Kerbin_DEV3/backend/models"
	"github.com/anirudhprabhakaran3/TRINIT_Valentina_Kerbin_DEV3/backend/services"
	"github.com/gin-gonic/gin"
)

func Login(c *gin.Context) {
	var req struct {
		Username string `json:"username" binding:"required"`
		Password string `json:"password" binding:"required"`
	}
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "incorrect parameters",
		})
		return
	}

	fmt.Println(req.Username)
	fmt.Println(req.Password)

	user, err := models.FindUserbyUsername(req.Username)
	if err != nil {
		c.JSON(http.StatusNotFound, gin.H{
			"error": fmt.Sprintf("user %s not found", req.Username),
		})
		return
	}

	if user.Password != req.Password {
		c.JSON(http.StatusUnauthorized, gin.H{
			"error": "incorrect password",
		})
		return
	}

	token, err := services.GenerateToken(*user)
	if err != nil {
		c.JSON(http.StatusUnauthorized, gin.H{
			"error": err.Error(),
		})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"token": token,
	})
}

func Register(c *gin.Context) {
	var req struct {
		Username    string `json:"username" binding:"required"`
		Password    string `json:"password" binding:"required"`
		Age         uint   `json:"age" binding:"required"`
		Email       string `json:"email" binding:"required"`
		Name        string `json:"name" binding:"required"`
		AccountType bool   `json:"accounttype" binding:"required"`
	}

	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error":   "incorrect parameters",
			"details": err.Error(),
		})
		return
	}

	_, err := models.InsertUser(
		req.Username,
		req.Password,
		req.Age,
		req.Email,
		req.Name,
		req.AccountType,
	)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "incorrect parameters",
		})
		return
	}

	c.JSON(http.StatusCreated, gin.H{
		"message": "user created",
	})
}

func GetUserInfo(c *gin.Context) {
	id, _, ok := services.GetSession(c)
	if !ok {
		c.JSON(http.StatusUnauthorized, gin.H{})
		return
	}

	user, err := models.FindUserByID(id)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}

	c.JSON(http.StatusOK, user)
}
