import { FaFacebook } from "react-icons/fa";
import { AiFillInstagram } from "react-icons/ai";
import { FaCircle } from "react-icons/fa6";
import { FaPinterest } from "react-icons/fa";
import { FaHome } from "react-icons/fa";
import { BsTwitterX } from "react-icons/bs";
import styled, { keyframes } from "styled-components";
import { mobile } from "../responsive";
import { IoCall, IoMail } from "react-icons/io5";

const Container = styled.div`
  display: flex;
  ${mobile({ flexDirection: "column" })}
`;

const Left = styled.div`
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 20px;
`;

const Logo = styled.h1``;

const Desc = styled.p`
  margin: 20px 0px;
`;

const SocialContainer = styled.div`
  display: flex;
`;

const SocialIcon = styled.div`
  width: 40px;
  height: 40px;
  border-radius: 50%;
  color: white;
  background-color: #${(props) => props.color};
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 20px;
`;

const Center = styled.div`
  flex: 1;
  padding: 20px;
  ${mobile({ display: "none" })}
`;

const Title = styled.h3`
  margin-bottom: 30px;
  color: #da0049
`;

const List = styled.ul`
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-wrap: wrap;
`;

const ListItem = styled.li`
  width: 50%;
  margin-bottom: 10px;
  cursor: pointer
`;

const Right = styled.div`
  flex: 1;
  padding: 20px;
  ${mobile({ backgroundColor: "#fff8f8" })}

`;

const ContactItem = styled.div`
  margin-bottom: 20px;
  display: flex;
  align-items: center;
`;

// Keyframes tanımı
const flicker = keyframes`
  0%, 80%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
`;

const FlickeringText = styled.span`
  animation: ${flicker} 1s infinite;
  color: #9e0437  ;
`;

const Footer = () => {
  return (
    <Container>
      <Left>
        <SocialContainer>
          <SocialIcon color="3B5999">
            <FaFacebook size={21} />
          </SocialIcon>
          <SocialIcon color="E4405F">
            <AiFillInstagram size={24} />
          </SocialIcon>
          <SocialIcon color="55ACEE">
            <BsTwitterX />
          </SocialIcon>
          <SocialIcon color="E60023">
            <FaPinterest size={22} />
          </SocialIcon>
        </SocialContainer>
      </Left>
      <Center>
        <List>
          <ListItem>Ana Sayfa</ListItem>
          <ListItem>Kategoriler</ListItem>
          <ListItem>Hesabım</ListItem>
          <ListItem>Sepetim</ListItem>
          <ListItem>Destek</ListItem>
          <ListItem>Talep ve Öneri</ListItem>
        </List>
      </Center>
      <Right>
        <ContactItem>
          <FaHome style={{ marginRight: "10px", color: "#9e0437" }} /> Gemlik/BURSA
        </ContactItem>
        <ContactItem>
          <IoCall style={{ marginRight: "10px", color: "#9e0437" }} /> 0812 123 12 12
        </ContactItem>
        <ContactItem>
          <IoMail style={{ marginRight: "10px", color: "#9e0437" }} /> antikadunyam_crazyboy@hotmail.com
        </ContactItem>
      </Right>
    </Container>
  );
};

export default Footer;
