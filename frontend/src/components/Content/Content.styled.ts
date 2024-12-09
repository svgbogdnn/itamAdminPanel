import styled from "styled-components";

export const Container = styled.div`
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 18px;
`;

export const FormContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  gap: 32px;
  min-width: 296px;
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 0 20px 0 #60E2FF;
`;

export const Title = styled.p`
  margin: 0;
  color: #56FF9E;
  font-family: Actay Wide;
  font-size: 20px;
  font-weight: 700;
  line-height: 1.26;
  text-transform: uppercase;
`;

export const Links = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  gap: 10px;
`;
