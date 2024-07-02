import { IoLogInOutline } from "react-icons/io5";
import { IoSearch } from "react-icons/io5";
import styled, { keyframes } from "styled-components";
import { mobile } from "../responsive";
import { RiUserAddLine } from "react-icons/ri";
import { IoCartOutline } from "react-icons/io5";
import { FaCircle } from "react-icons/fa6";





const Container = styled.div`
  height: 60px;
  ${mobile({ height: "50px" })}
`;

const Wrapper = styled.div`
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  ${mobile({ padding: "10px 15px 0px 0px" })}
`;

const Left = styled.div`
  flex: 1;
  display: flex;
  align-items: center;
`;

const Language = styled.span`
  font-size: 14px;
  cursor: pointer;
  ${mobile({ display: "none" })}
`;

const SearchContainer = styled.div`
  border: 0.5px solid lightgray;
  display: flex;
  align-items: center;
  margin-left: 25px;
  padding: 5px;
  ${mobile({ marginLeft: "10px" })}
  `;

const Input = styled.input`
  border: none;
  ${mobile({ width: "55px", fontSize: "11px" })}
  &:focus {
  outline: none;
}
`;

const Center = styled.div`
  flex: 1;
  text-align: center;
`;

const Logo = styled.h1`
  text-align: center;
  font-weight: bold;
  ${mobile({ fontSize: "20px", marginLeft: "5px" })}
`;
const Right = styled.div`
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  ${mobile({ flex: 2, justifyContent: "center", marginLeft: "10px" })}
`;

const MenuItem = styled.div`
  font-size: 14px;
  cursor: pointer;
  margin-left: 25px;
  ${mobile({ fontSize: "9px", marginLeft: "2px" })}
`;


const CartIconContainer = styled.div`
  position: relative;
`;


const Badge = styled.span`
  position: absolute;
  top: -10px;
  right: -10px;
  background-color: brown;
  color: white;
  border-radius: 50%;
  padding: 2px; /* padding değeri artırıldı */
  padding-top: 3px;
  padding-bottom: 3px;
  font-size: 13px;
  min-width: 18px; /* minimum genişlik eklendi */
  text-align: center;
  font-size: 12px;
  ${mobile({ fontSize: "10px", marginTop: "5px" })}
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
  color: #9e0437;
`;

const Navbar = () => {
  return (
    <Container>
      <Wrapper>
        <Left>
          <SearchContainer>
            <Input placeholder="Ürün Ara" />
            <IoSearch style={{ color: "brown", fontSize: 16 }} />
          </SearchContainer>
        </Left>
        <Center>
          <Logo>ANTİKA DÜNYAM<FlickeringText></FlickeringText></Logo >
        </Center>
        <Right>
          <MenuItem style={{ marginRight: "2px" }}>KAYIT OL </MenuItem>
          <RiUserAddLine size={18} />
          <MenuItem style={{ marginRight: "2px" }}>GİRİŞ YAP </MenuItem>
          <IoLogInOutline size={22} />
          <MenuItem>
            <CartIconContainer>
              <IoCartOutline size={27} />
              <Badge>{2}</Badge>
            </CartIconContainer>
          </MenuItem>
        </Right>
      </Wrapper>
    </Container >
  );
};

export default Navbar;
