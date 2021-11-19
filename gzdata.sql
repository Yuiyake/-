/*
 Navicat Premium Data Transfer

 Source Server         : yuiyake
 Source Server Type    : MySQL
 Source Server Version : 80024
 Source Host           : localhost:3306
 Source Schema         : catchdata

 Target Server Type    : MySQL
 Target Server Version : 80024
 File Encoding         : 65001

 Date: 19/11/2021 11:32:56
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for gzdata
-- ----------------------------
DROP TABLE IF EXISTS `gzdata`;
CREATE TABLE `gzdata`  (
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `wuye` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `states` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `location` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `jishi` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `area` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tag` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `price` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `totalprice` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `imgurl` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of gzdata
-- ----------------------------
INSERT INTO `gzdata` VALUES ('碧桂园荔山雅筑', '住宅', '在售', '从化/赤草/广从公路(105国道) 赤草地铁站旁400米', '3室', '109-120㎡', '地铁沿线多轨交汇购物方便美食云集', '14000', '总价150-175(万/套)', 'https://image1.ljcdn.com/hdic-resblock/7a21230a-9cbc-486f-8d45-ec413e5a83e8.jpg.592x432.jpg');
INSERT INTO `gzdata` VALUES ('景业东湖洲豪园', '住宅', '在售', '南沙/南沙湾/广东省广州市南沙区环市大道南横地铁站200米', '3室', '95-121㎡', '地铁沿线多轨交汇成熟商圈配套齐全', '28000', '总价320-330(万/套)', 'https://image1.ljcdn.com/hdic-resblock/d634a2c1-06e4-458b-91e9-840a0569d8f4.jpg.592x432.jpg');
INSERT INTO `gzdata` VALUES ('保利半岛', '住宅', '在售', '南沙/黄阁/南沙区东逸三路与市南大道交叉路口往北200米（南沙区滨水大道东西侧）', '4室', '99-133㎡', '公交直达近主干道成熟商圈购物方便', '34000', '总价400(万/套)', 'https://image1.ljcdn.com/hdic-resblock/54bc0e98-b5f7-48d0-9d06-877bf2aa86e3.jpg.592x432.jpg');
INSERT INTO `gzdata` VALUES ('绿地云央', '住宅', '在售', '白云/太和/草塘路5号', '3室', '98-138㎡', '低单价低总价公交直达近主干道', '27000', '总价270-360(万/套)', 'https://image1.ljcdn.com/hdic-resblock/d43ed7ca-1591-4cf4-b12f-8316861351a1.jpg.592x432.jpg');
INSERT INTO `gzdata` VALUES ('南沙珠江湾', '商业', '在售', '南沙/南沙湾/漾滨路和海滨路交汇处', '', '暂无', '低总价地铁沿线公交直达配套齐全', '30000', '总价318(万/套)', 'https://image1.ljcdn.com/hdic-resblock/d47ad6a5-5901-4cfa-abc6-08a2797412f3.jpg.592x432.jpg');
INSERT INTO `gzdata` VALUES ('碧桂园云顶', '住宅', '在售', '增城/凤凰城/广东省广州市增城区广惠高速路口西侧50米', '3室/4室/5室', '90-205㎡', '公交直达购物方便超市医疗配套', '28000', '总价225-650(万/套)', 'https://image1.ljcdn.com/newhouse-user-image/296dc981c6000c8a1328cb256dc044a5.jpg.592x432.jpg');
INSERT INTO `gzdata` VALUES ('西关海', '住宅', '在售', '荔湾/南岸路/南岸路23号（青年公园旁）', '2室', '87-310㎡', '地铁沿线近主干道成熟商圈配套齐全', '72000', '总价600(万/套)', 'https://image1.ljcdn.com/hdic-resblock/b33629f4-e432-4077-b511-d7846e05e98f.jpg.592x432.jpg');
INSERT INTO `gzdata` VALUES ('智杰雅筑', '住宅', '在售', '从化/河滨北路/向阳路32号', '3室/5室', '90-242㎡', '低总价地铁沿线公交直达成熟商圈', '15000', '总价145-390(万/套)', 'https://image1.ljcdn.com/hdic-resblock/5f881493-a302-4e7b-a999-852746d9fd82.jpg.592x432.jpg');
INSERT INTO `gzdata` VALUES ('新世界凯粤湾', '住宅', '在售', '荔湾/滘口/芳村大道西236号', '2室/3室/4室', '79-143㎡', '低总价地铁沿线近主干道成熟商圈', '50000', '总价395-715(万/套)', 'https://image1.ljcdn.com/hdic-resblock/fd505918-1054-4c5c-b9cf-38a021508ad7.jpg.592x432.jpg');
INSERT INTO `gzdata` VALUES ('南华时代城', '住宅', '在售', '花都/旧区/新华街工业大道18号', '3室', '105-124㎡', '低总价地铁沿线临近高速成熟商圈', '20000', '总价210-248(万/套)', 'https://image1.ljcdn.com/hdic-resblock/001cbddd-ffd1-4623-9285-ec4792226ac3.jpg.592x432.jpg');

SET FOREIGN_KEY_CHECKS = 1;
