import React, {Component} from 'react';
import PropTypes from "prop-types";
import {StyleSheet, Text, View, TextInput, FlatList, Picker, ScrollView, TouchableHighlight} from 'react-native';
import {Image as ReactImage} from 'react-native';
import Svg, {Defs, Pattern} from 'react-native-svg';
import {Path as SvgPath} from 'react-native-svg';
import {Text as SvgText} from 'react-native-svg';
import {Image as SvgImage} from 'react-native-svg';

export default class About extends Component {

  constructor(props) {
      super(props);
      this.state = {
          
      };
  }


  handlePress(target, owner) {
    if (this.props.onPress) {
        let name;
        let id;
        let index = -1;
        if (target.search("::") > -1) {
            const varCount = target.split("::").length;
            if (varCount === 2) {
                name = target.split("::")[0];
                id = target.split("::")[1];
            } else if (varCount === 3) {
                name = target.split("::")[0];
                index = parseInt(target.split("::")[1]);
                id = target.split("::")[2];
            }
        } else {
            name = target;
        }
        this.props.onPress({ type: 'button', name: name, index: index, id: id, owner: owner });
    }
  }

  handleChangeTextinput(name, value) {
      let id;
      let index = -1;
      if (name.search('::') > -1) {
          const varCount = name.split("::").length;
          if (varCount === 2) {
              name = name.split("::")[0];
              id = name.split("::")[1];
          } else if (varCount === 3) {
              name = name.split("::")[0];
              index = name.split("::")[1];
              id = name.split("::")[2];
          }
      } else {
          name = name;
      }
      let state = this.state;
      state[name.split('::').join('')] = value;
      this.setState(state, () => {
          if (this.props.onChange) {
              this.props.onChange({ type: 'textinput', name: name, value: value, index: index, id: id });
          }
      });
  }

  render() {
    
    return (
    <ScrollView data-layer="715207c6-0f83-4a75-999b-c8badb8a2b9d" style={styles.about}>
        <ReactImage data-layer="bc96a20a-599c-4e55-a959-6068dedb8005" source={require('./assets/x02laughing.png')} style={styles.about_x02laughing} />
        <ReactImage data-layer="074e2ed9-eb71-4316-9f8b-8eeaa5e0e027" source={require('./assets/rectangle1.png')} style={styles.about_rectangle1} />
        <View data-layer="66ce7cb2-9843-4f82-a917-c8610a13f098" style={styles.about_frame167578d4}></View>
        <View data-layer="9d01d2d3-1dc2-4a39-9780-a599936be56c" style={styles.about_statusBar}>
            <View data-layer="11bc6519-a48e-4414-b093-04cd080114be" style={styles.about_statusBar_battery}>
                <View data-layer="cbf1a7c3-3a32-4c96-8553-5c25febd0c4b" style={styles.about_statusBar_battery_border}></View>
                <Svg data-layer="2b03f89e-bf72-4eb9-97e7-35aa7c3b9dc5" style={styles.about_statusBar_battery_cap} preserveAspectRatio="none" viewBox="-0.75 -0.75 2.8280029296875 5.5" fill="rgba(255, 255, 255, 1)"><SvgPath d="M 0 0 L 0 4 C 0.8047311305999756 3.661223411560059 1.328037977218628 2.873133182525635 1.328037977218628 2 C 1.328037977218628 1.126866698265076 0.8047311305999756 0.3387765288352966 0 0"  /></Svg>
                <View data-layer="91b20d9b-1192-4292-8846-d2cf051d211b" style={styles.about_statusBar_battery_capacity}></View>
            </View>
            <Svg data-layer="b4de642e-3a1d-429c-95e3-faa6594faace" style={styles.about_statusBar_wifi} preserveAspectRatio="none" viewBox="-0.7500179782509804 -0.7499996589660611 16.8333740234375 12.499801635742188" fill="rgba(255, 255, 255, 1)"><SvgPath d="M 7.667099952697754 10.99980068206787 C 7.583849906921387 10.99980068206787 7.502830028533936 10.96601009368896 7.444799900054932 10.90710067749023 L 5.438699722290039 8.884799957275391 C 5.376539707183838 8.824450492858887 5.342419624328613 8.740139961242676 5.345099925994873 8.653500556945801 C 5.34689998626709 8.567130088806152 5.38461971282959 8.48445987701416 5.448599815368652 8.426700592041016 C 6.068009853363037 7.903050422668457 6.855879783630371 7.614680290222168 7.667099952697754 7.614680290222168 C 8.478329658508301 7.614680290222168 9.266200065612793 7.903060436248779 9.885600090026855 8.426700592041016 C 9.949589729309082 8.48445987701416 9.987299919128418 8.567120552062988 9.989099502563477 8.653500556945801 C 9.990900039672852 8.740429878234863 9.956449508666992 8.824740409851074 9.894599914550781 8.884799957275391 L 7.889400005340576 10.90710067749023 C 7.831369876861572 10.96601009368896 7.750349998474121 10.99980068206787 7.667099952697754 10.99980068206787 Z M 11.18970012664795 7.45110034942627 C 11.10974979400635 7.45110034942627 11.03334999084473 7.420740127563477 10.97459983825684 7.365600109100342 C 10.06602954864502 6.544380187988281 8.891399383544922 6.092100143432617 7.667099952697754 6.092100143432617 C 6.443639755249023 6.093000411987305 5.269969940185547 6.545270442962646 4.362299919128418 7.365600109100342 C 4.303549766540527 7.420730113983154 4.227149963378906 7.45110034942627 4.147199630737305 7.45110034942627 C 4.064209938049316 7.45110034942627 3.986219882965088 7.418820381164551 3.927599906921387 7.36020040512085 L 2.768399715423584 6.189300537109375 C 2.706559896469116 6.127450466156006 2.672999858856201 6.04563045501709 2.67389988899231 5.958900451660156 C 2.674789905548096 5.871150493621826 2.709949731826782 5.789650440216064 2.772899866104126 5.729400157928467 C 4.106770038604736 4.489140510559082 5.845219612121582 3.806100368499756 7.667999744415283 3.806100368499756 C 9.490459442138672 3.806100368499756 11.22922992706299 4.489140510559082 12.56400012969971 5.729400157928467 C 12.62695026397705 5.790550231933594 12.662109375 5.872050285339355 12.66300010681152 5.958900451660156 C 12.66389942169189 6.04563045501709 12.63033962249756 6.127450466156006 12.56849956512451 6.189300537109375 L 11.40929985046387 7.36020040512085 C 11.35066986083984 7.418820381164551 11.27268981933594 7.45110034942627 11.18970012664795 7.45110034942627 Z M 13.85909938812256 4.758300304412842 C 13.77816963195801 4.758300304412842 13.70177936553955 4.726980209350586 13.64400005340576 4.670100212097168 C 12.02444934844971 3.131530284881592 9.901809692382813 2.284200429916382 7.667099952697754 2.284200429916382 C 5.431809902191162 2.284200429916382 3.308849811553955 3.131530284881592 1.689299821853638 4.67011022567749 C 1.631529808044434 4.726970195770264 1.555129766464233 4.758300304412842 1.474199771881104 4.758300304412842 C 1.390889763832092 4.758300304412842 1.312899827957153 4.725700378417969 1.254599809646606 4.666500568389893 L 0.09359981864690781 3.496500253677368 C 0.03233981877565384 3.434340238571167 -0.0009001815924420953 3.352830410003662 -1.815795940274256e-07 3.267000436782837 C 0.0008998184348456562 3.180460453033447 0.0350998193025589 3.099590301513672 0.09629981964826584 3.039300441741943 C 2.143509864807129 1.079370379447937 4.832200050354004 3.410339388665307e-07 7.667099952697754 3.410339388665307e-07 C 10.50232028961182 3.410339388665307e-07 13.19069004058838 1.079380393028259 15.23699951171875 3.039300441741943 C 15.29819965362549 3.099590301513672 15.33239936828613 3.180460453033447 15.33329963684082 3.267000436782837 C 15.33419990539551 3.352830410003662 15.30095958709717 3.434340238571167 15.2396993637085 3.496500253677368 L 14.07870006561279 4.666500568389893 C 14.02040004730225 4.725700378417969 13.94240951538086 4.758300304412842 13.85909938812256 4.758300304412842 Z"  /></Svg>
            <Svg data-layer="7c17f294-cc58-4b50-a12f-2e4a818fa507" style={styles.about_statusBar_cellularConnection} preserveAspectRatio="none" viewBox="-0.7499994552612179 -0.7499998211860657 18.5001220703125 12.166801452636719" fill="rgba(255, 255, 255, 1)"><SvgPath d="M 16.00020027160645 10.6668004989624 L 15.00030040740967 10.6668004989624 C 14.44895076751709 10.6668004989624 14.00040054321289 10.2182502746582 14.00040054321289 9.666900634765625 L 14.00040054321289 0.999900221824646 C 14.00040054321289 0.4485502541065216 14.44895076751709 2.494811894848681e-07 15.00030040740967 2.494811894848681e-07 L 16.00020027160645 2.494811894848681e-07 C 16.55154991149902 2.494811894848681e-07 17.00010108947754 0.4485502541065216 17.00010108947754 0.999900221824646 L 17.00010108947754 9.666900634765625 C 17.00010108947754 10.2182502746582 16.55154991149902 10.6668004989624 16.00020027160645 10.6668004989624 Z M 11.33370018005371 10.6668004989624 L 10.33290100097656 10.6668004989624 C 9.781550407409668 10.6668004989624 9.333000183105469 10.2182502746582 9.333000183105469 9.666900634765625 L 9.333000183105469 3.333600282669067 C 9.333000183105469 2.782250165939331 9.781550407409668 2.333700180053711 10.33290100097656 2.333700180053711 L 11.33370018005371 2.333700180053711 C 11.88505077362061 2.333700180053711 12.3336009979248 2.782250165939331 12.3336009979248 3.333600282669067 L 12.3336009979248 9.666900634765625 C 12.3336009979248 10.2182502746582 11.88505077362061 10.6668004989624 11.33370018005371 10.6668004989624 Z M 6.666300773620605 10.6668004989624 L 5.66640043258667 10.6668004989624 C 5.115050315856934 10.6668004989624 4.666500568389893 10.2182502746582 4.666500568389893 9.666900634765625 L 4.666500568389893 5.66640043258667 C 4.666500568389893 5.115050315856934 5.115050315856934 4.666500091552734 5.66640043258667 4.666500091552734 L 6.666300773620605 4.666500091552734 C 7.218140602111816 4.666500091552734 7.667100429534912 5.115050315856934 7.667100429534912 5.66640043258667 L 7.667100429534912 9.666900634765625 C 7.667100429534912 10.2182502746582 7.218140602111816 10.6668004989624 6.666300773620605 10.6668004989624 Z M 1.999800562858582 10.6668004989624 L 0.9999005198478699 10.6668004989624 C 0.4485505521297455 10.6668004989624 5.447387820822769e-07 10.2182502746582 5.447387820822769e-07 9.666900634765625 L 5.447387820822769e-07 7.667100429534912 C 5.447387820822769e-07 7.115260124206543 0.4485505521297455 6.666300296783447 0.9999005198478699 6.666300296783447 L 1.999800562858582 6.666300296783447 C 2.551150560379028 6.666300296783447 2.999700546264648 7.115260124206543 2.999700546264648 7.667100429534912 L 2.999700546264648 9.666900634765625 C 2.999700546264648 10.2182502746582 2.551150560379028 10.6668004989624 1.999800562858582 10.6668004989624 Z"  /></Svg>
            <View data-layer="5a9404b1-8626-4fd1-8589-5ab21c88edc0" style={styles.about_statusBar_timeStyle}>
                <Text data-layer="f4c0f8ca-68a3-4581-bca8-367fc38b9efa" style={styles.about_statusBar_timeStyle_time}>9:41</Text>
            </View>
        </View>
        <Svg data-layer="1ec07a02-3e43-4432-927f-ca6bde5ba6da" style={styles.about_x02smile} preserveAspectRatio="none" viewBox="-2.25 -2.25 165.96429443359375 155.25" fill="rgba(255, 255, 255, 0)"><Defs><Pattern id="img-x02smile" patternContentUnits="userSpaceOnUse" width="100%" height="100%"><SvgImage xlinkHref={require('./assets/x02smile.png')} x="0" y="0" width="160.71px" height="150.00px" /></Pattern></Defs><SvgPath d="M 80.35713958740234 0 C 124.7371597290039 0 160.7142791748047 33.57864761352539 160.7142791748047 75 C 160.7142791748047 116.4213562011719 124.7371597290039 150 80.35713958740234 150 C 35.97711944580078 150 0 116.4213562011719 0 75 C 0 33.57864761352539 35.97711944580078 0 80.35713958740234 0 Z" fill="url(#img-x02smile)" /></Svg>
        <Text data-layer="97b3a583-040f-4254-bbff-42aadcd9a7fc" style={styles.about_zeroTwo}>Zero Two</Text>
        <Text data-layer="40ad3214-1bc9-470b-add5-d67fcb75c931" style={styles.about_apeSpecialOps}>APE Special Ops</Text>
        <Text data-layer="1b609df9-fae6-4a94-a2eb-cef165c9789e" style={styles.about_parasite}>Parasite</Text>
        <Svg data-layer="ec95eece-7125-4f5c-b410-6b2ec26138ea" style={styles.about_line1} preserveAspectRatio="none" viewBox="-1 0 2 16" fill="transparent"><SvgPath d="M 0 0 L 0 16"  /></Svg>
        <Text data-layer="f5f3a73b-01d8-41b6-bbd7-2300433b8502" style={styles.about_profileb0253c68}>Profile</Text>
        <Text data-layer="c10e8983-bc20-46b3-8771-b945ad1f0849" style={styles.about_aboutb40aa9f5}>About</Text>
        <Svg data-layer="a239e82b-e13c-43a7-95d3-0f5b3c7324f2" style={styles.about_line2} preserveAspectRatio="none" viewBox="0 -2.5 187 5" fill="transparent"><SvgPath d="M 0 0 L 187 0"  /></Svg>
        <View data-layer="9a6bbfeb-f5d9-4293-89ee-8216e6a44be2" style={styles.about_rectangle2}></View>
        <Text data-layer="92f2ac2d-cf57-436f-9841-3d140f6a887d" style={styles.about_follow}>Follow</Text>
        <View data-layer="dabf94d6-3fe2-4206-b530-00f47c53334e" style={styles.about_group4}>
            <ReactImage data-layer="a6a18fd4-4254-4ce0-9dcb-8924c8b89c55" source={require('./assets/zeroTwoFeature.png')} style={styles.about_group4_zeroTwoFeature} />
            <Svg data-layer="cae99cb0-7cb9-4993-a6fb-9e646a67b34f" style={styles.about_group4_polygon1} preserveAspectRatio="none" viewBox="0 0 75 65" fill="rgba(255, 255, 255, 1)"><SvgPath d="M 37.49999618530273 0 L 75 65 L 0 65 Z"  /></Svg>
        </View>
        <View data-layer="7e2f6e4a-ab3e-4aba-8fb6-9cf1bc35cdc2" style={styles.about_group5}>
            <ReactImage data-layer="2e5aaf86-acea-49f8-9631-6402b4f5984e" source={require('./assets/rectangle78dcec7cc.png')} style={styles.about_group5_rectangle78dcec7cc} />
            <Text data-layer="0342a1a0-6af1-4d55-89c4-4d476291721b" style={styles.about_group5_featuredVideo}>Featured Video</Text>
        </View>
        <View data-layer="916903f3-7d02-41b5-a10c-ef932a4840f5" style={styles.about_group6}>
            <ReactImage data-layer="fbabfd97-af83-4a0a-9626-e1d2d755df76" source={require('./assets/rectangle7e0b0b399.png')} style={styles.about_group6_rectangle7e0b0b399} />
            <Text data-layer="449d1e3b-70dc-42ec-9382-046b4e13ab29" style={styles.about_group6_following}>Following</Text>
        </View>
        <ScrollView data-layer="195b4dc0-1f0f-4701-862f-8ad8bbf20a6c" style={styles.about_repeatGrid2}>
            <View data-layer="5912f6c1-3f85-42e2-822f-790301e32641" style={styles.about_repeatGrid2_repeatGrid254d0e28822bd}>
                <Svg data-layer="308c32fc-3fa3-46ed-b692-c1587acda4ac" style={styles.about_repeatGrid2_repeatGrid254d0e28822bd_goro} preserveAspectRatio="none" viewBox="-0.75 -0.75 56.5 56.5" fill="rgba(255, 255, 255, 0)"><Defs><Pattern id="img-goro" patternContentUnits="userSpaceOnUse" width="100%" height="100%"><SvgImage xlinkHref={require('./assets/goro.png')} x="0" y="0" width="55.00px" height="55.00px" /></Pattern></Defs><SvgPath d="M 27.5 0 C 42.68782806396484 0 55 12.31217098236084 55 27.5 C 55 42.68782806396484 42.68782806396484 55 27.5 55 C 12.31217098236084 55 0 42.68782806396484 0 27.5 C 0 12.31217098236084 12.31217098236084 0 27.5 0 Z" fill="url(#img-goro)" /></Svg>
                <Text data-layer="a096517a-9db6-4893-b704-c8db996fe5bb" style={styles.about_repeatGrid2_repeatGrid254d0e28822bd_characters}>Goro</Text>
            </View>
            <View data-layer="c8873630-c869-4724-903d-4ecdde0bf8bf" style={styles.about_repeatGrid2_repeatGrid20fd38bc26e24}>
                <Svg data-layer="e15f77f3-8a31-405f-b793-2c28b7669f0f" style={styles.about_repeatGrid2_repeatGrid20fd38bc26e24_hiro91e722e3} preserveAspectRatio="none" viewBox="-0.75 -0.75 56.5 56.5" fill="rgba(255, 255, 255, 0)"><Defs><Pattern id="img-hiro91e722e3" patternContentUnits="userSpaceOnUse" width="100%" height="100%"><SvgImage xlinkHref={require('./assets/hiro91e722e3.png')} x="0" y="0" width="55.00px" height="55.00px" /></Pattern></Defs><SvgPath d="M 27.5 0 C 42.68782806396484 0 55 12.31217098236084 55 27.5 C 55 42.68782806396484 42.68782806396484 55 27.5 55 C 12.31217098236084 55 0 42.68782806396484 0 27.5 C 0 12.31217098236084 12.31217098236084 0 27.5 0 Z" fill="url(#img-hiro91e722e3)" /></Svg>
                <Text data-layer="51019fae-df97-48fb-9175-1817edb8decf" style={styles.about_repeatGrid2_repeatGrid20fd38bc26e24_ichigob080c1ed}>Hiro</Text>
            </View>
            <View data-layer="3c1bcbc7-119f-470f-a552-035409ddc1a5" style={styles.about_repeatGrid2_repeatGrid244eb61dd0fd4}>
                <Svg data-layer="2ec7c7cd-9224-4acc-9c6e-72f2b3375fe8" style={styles.about_repeatGrid2_repeatGrid244eb61dd0fd4_hiroaa575910} preserveAspectRatio="none" viewBox="-0.75 -0.75 56.5 56.5" fill="rgba(255, 255, 255, 0)"><Defs><Pattern id="img-hiroaa575910" patternContentUnits="userSpaceOnUse" width="100%" height="100%"><SvgImage xlinkHref={require('./assets/hiroaa575910.png')} x="0" y="0" width="55.00px" height="55.00px" /></Pattern></Defs><SvgPath d="M 27.5 0 C 42.68782806396484 0 55 12.31217098236084 55 27.5 C 55 42.68782806396484 42.68782806396484 55 27.5 55 C 12.31217098236084 55 0 42.68782806396484 0 27.5 C 0 12.31217098236084 12.31217098236084 0 27.5 0 Z" fill="url(#img-hiroaa575910)" /></Svg>
                <Text data-layer="3925cc3c-58e8-4cd0-bedf-3877352c7bcf" style={styles.about_repeatGrid2_repeatGrid244eb61dd0fd4_ichigod68334a6}>Ichigo</Text>
            </View>
            <View data-layer="0621c92d-7fea-40df-bc07-dd0acdaf6c36" style={styles.about_repeatGrid2_repeatGrid2159e3899a1f1}>
                <Svg data-layer="02e3c01b-0496-470f-a389-6d0785e9367d" style={styles.about_repeatGrid2_repeatGrid2159e3899a1f1_hiro56a49510} preserveAspectRatio="none" viewBox="-0.75 -0.75 56.5 56.5" fill="rgba(255, 255, 255, 0)"><Defs><Pattern id="img-hiro56a49510" patternContentUnits="userSpaceOnUse" width="100%" height="100%"><SvgImage xlinkHref={require('./assets/hiro56a49510.png')} x="0" y="0" width="55.00px" height="55.00px" /></Pattern></Defs><SvgPath d="M 27.5 0 C 42.68782806396484 0 55 12.31217098236084 55 27.5 C 55 42.68782806396484 42.68782806396484 55 27.5 55 C 12.31217098236084 55 0 42.68782806396484 0 27.5 C 0 12.31217098236084 12.31217098236084 0 27.5 0 Z" fill="url(#img-hiro56a49510)" /></Svg>
                <Text data-layer="b9dc512c-cf38-4f79-9947-c29eb9a8bbbe" style={styles.about_repeatGrid2_repeatGrid2159e3899a1f1_ichigo5914f51a}>Ikuno</Text>
            </View>
            <View data-layer="74bab12f-dc4f-492e-ad0e-bead6b485734" style={styles.about_repeatGrid2_repeatGrid2138e6e86d200}>
                <Svg data-layer="cf54cba7-ed0a-4942-8b1e-2a00fea75537" style={styles.about_repeatGrid2_repeatGrid2138e6e86d200_hiro95307941} preserveAspectRatio="none" viewBox="-0.75 -0.75 56.5 56.5" fill="rgba(255, 255, 255, 0)"><Defs><Pattern id="img-hiro95307941" patternContentUnits="userSpaceOnUse" width="100%" height="100%"><SvgImage xlinkHref={require('./assets/hiro95307941.png')} x="0" y="0" width="55.00px" height="55.00px" /></Pattern></Defs><SvgPath d="M 27.5 0 C 42.68782806396484 0 55 12.31217098236084 55 27.5 C 55 42.68782806396484 42.68782806396484 55 27.5 55 C 12.31217098236084 55 0 42.68782806396484 0 27.5 C 0 12.31217098236084 12.31217098236084 0 27.5 0 Z" fill="url(#img-hiro95307941)" /></Svg>
                <Text data-layer="61cf54cd-f9f1-4730-9fac-93cafd2636c2" style={styles.about_repeatGrid2_repeatGrid2138e6e86d200_ichigo57d965be}>Miku</Text>
            </View>
            <View data-layer="71e8a803-b84a-43b1-a403-c82028283389" style={styles.about_repeatGrid2_repeatGrid2Eef815140c8c}>
                <Svg data-layer="078eeb23-9bb6-40ac-bb41-9b72e23b5352" style={styles.about_repeatGrid2_repeatGrid2Eef815140c8c_hiro} preserveAspectRatio="none" viewBox="-0.75 -0.75 56.5 56.5" fill="rgba(255, 255, 255, 0)"><Defs><Pattern id="img-hiro" patternContentUnits="userSpaceOnUse" width="100%" height="100%"><SvgImage xlinkHref={require('./assets/hiro.png')} x="0" y="0" width="55.00px" height="55.00px" /></Pattern></Defs><SvgPath d="M 27.5 0 C 42.68782806396484 0 55 12.31217098236084 55 27.5 C 55 42.68782806396484 42.68782806396484 55 27.5 55 C 12.31217098236084 55 0 42.68782806396484 0 27.5 C 0 12.31217098236084 12.31217098236084 0 27.5 0 Z" fill="url(#img-hiro)" /></Svg>
                <Text data-layer="61ef5cd0-9e78-4d51-9e4f-898f46d80ae8" style={styles.about_repeatGrid2_repeatGrid2Eef815140c8c_ichigo}>Zorome</Text>
            </View>
        </ScrollView>
        <View data-layer="6ba3fc63-bbe4-4866-a24e-548c33eb4626" style={styles.about_group7}>
            <ReactImage data-layer="1a054ea4-c8a0-4ef2-b03d-ff8be483e001" source={require('./assets/rectangle7.png')} style={styles.about_group7_rectangle7} />
            <Text data-layer="dfe1dc9d-ff82-45c3-a1a7-f94913240c28" style={styles.about_group7_background0d9e790e}>Background</Text>
        </View>
        <Text data-layer="5c1e5038-a6f6-4a60-8bfc-81a168695e9e" style={styles.about_talkAboutYourselfInThisSectionTalkAboutYourLifeAndhowYouGotIntroducedIntoThisPlatformAndHowYouAreaGodNow}>Talk about yourself in this section. Talk about your life and
how you got introduced into this platform and how you are
a god now.</Text>
        <View data-layer="61a345a7-95b3-41ff-8b99-933a4ee8b748" style={styles.about_barsToolbarIphoneCompactDark3Glyphs}>
            <View data-layer="aec5c174-b20b-40bb-b6fc-04cb214ef2a3" style={styles.about_barsToolbarIphoneCompactDark3Glyphs_background5f27efc2}>
                <ReactImage data-layer="427b587a-c2c0-4411-9e80-9768e51cfd1e" source={require('./assets/background.png')} style={styles.about_barsToolbarIphoneCompactDark3Glyphs_background5f27efc2_background} />
            </View>
            <View data-layer="09ed9aa6-cce0-40e7-8768-914091761fc6" style={styles.about_barsToolbarIphoneCompactDark3Glyphs_profile}>
                <View data-layer="08e13619-6148-449b-a121-cdd66739edc3" style={styles.about_barsToolbarIphoneCompactDark3Glyphs_profile_framee4e32c60}></View>
                <View data-layer="ed833801-b9ba-47b0-b0d2-46a9ddc36aa9" style={styles.about_barsToolbarIphoneCompactDark3Glyphs_profile_group3}>
                    <Svg data-layer="e7ecd1c7-937b-4ef0-98a8-691bbcbfed89" style={styles.about_barsToolbarIphoneCompactDark3Glyphs_profile_group3_ellipse3} preserveAspectRatio="none" viewBox="0 0 25 24" fill="rgba(0, 0, 0, 1)"><SvgPath d="M 12.5 0 C 19.4035587310791 0 25 5.372583389282227 25 12 C 25 18.62741661071777 19.4035587310791 24 12.5 24 C 5.596441268920898 24 0 18.62741661071777 0 12 C 0 5.372583389282227 5.596441268920898 0 12.5 0 Z"  /></Svg>
                    <View data-layer="b54b96d6-702a-4b1e-b5d9-d8c0af8dcc13" style={styles.about_barsToolbarIphoneCompactDark3Glyphs_profile_group3_rectangle5}></View>
                    <View data-layer="97e7a8c4-beaa-4a29-9bf1-f6649aac2fdc" style={styles.about_barsToolbarIphoneCompactDark3Glyphs_profile_group3_rectangle6}></View>
                </View>
            </View>
            <View data-layer="36d00ee1-a233-4e75-af70-cfd2317063cd" style={styles.about_barsToolbarIphoneCompactDark3Glyphs_add}>
                <View data-layer="1d66b507-572b-4c1a-b1c5-cfb5186cdf03" style={styles.about_barsToolbarIphoneCompactDark3Glyphs_add_frame036c7384}></View>
                <View data-layer="f10f71df-9478-4562-a9a0-a9250d59156d" style={styles.about_barsToolbarIphoneCompactDark3Glyphs_add_group1}>
                    <View data-layer="45cd5277-1905-4769-be8f-5fca9db13f48" style={styles.about_barsToolbarIphoneCompactDark3Glyphs_add_group1_rectangle3}></View>
                    <Svg data-layer="3c012b0a-ab71-42fe-9764-901b91495db9" style={styles.about_barsToolbarIphoneCompactDark3Glyphs_add_group1_line3} preserveAspectRatio="none" viewBox="0 -1.5 40.28070068359375 3" fill="transparent"><SvgPath d="M 0 0 L 40.28070068359375 0"  /></Svg>
                    <Svg data-layer="49cf9105-63f3-45bc-b5a9-7ca392f5eae5" style={styles.about_barsToolbarIphoneCompactDark3Glyphs_add_group1_line4} preserveAspectRatio="none" viewBox="-1.5 0 3 41" fill="transparent"><SvgPath d="M 0 0 L 0 41"  /></Svg>
                </View>
            </View>
            <View data-layer="234c7a67-7ee0-4292-981a-3e76fe5b720c" style={styles.about_barsToolbarIphoneCompactDark3Glyphs_home}>
                <ReactImage data-layer="31ba44cd-93a3-45dd-be58-eede29e67f75" source={require('./assets/frame.png')} style={styles.about_barsToolbarIphoneCompactDark3Glyphs_home_frame} />
            </View>
        </View>
    </ScrollView>
    );
  }
}

About.propTypes = {

}

About.defaultProps = {

}


const styles = StyleSheet.create({
  "about": {
    "opacity": 1,
    "position": "relative",
    "backgroundColor": "rgba(143, 95, 95, 1)",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 375,
    "height": 1177,
    "left": 0,
    "top": 0
  },
  "about_x02laughing": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "borderTopLeftRadius": 0,
    "borderTopRightRadius": 0,
    "borderBottomLeftRadius": 0,
    "borderBottomRightRadius": 0,
    "width": 713,
    "height": 300,
    "left": -169,
    "top": -6
  },
  "about_rectangle1": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "borderTopLeftRadius": 0,
    "borderTopRightRadius": 0,
    "borderBottomLeftRadius": 0,
    "borderBottomRightRadius": 0,
    "width": 375,
    "height": 300,
    "left": 0,
    "top": -6
  },
  "about_frame167578d4": {
    "opacity": 0.0010436499724164605,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 1)",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "borderTopLeftRadius": 0,
    "borderTopRightRadius": 0,
    "borderBottomLeftRadius": 0,
    "borderBottomRightRadius": 0,
    "width": 375,
    "height": 44,
    "left": 0,
    "top": 0
  },
  "about_statusBar": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 339.66,
    "height": 18,
    "left": 5,
    "top": 7
  },
  "about_statusBar_battery": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 24.33,
    "height": 11.33,
    "left": 315.33,
    "top": 3.33
  },
  "about_statusBar_battery_border": {
    "opacity": 0.3499999940395355,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "borderTopWidth": 1,
    "borderTopColor": "rgba(255, 255, 255, 1)",
    "borderRightWidth": 1,
    "borderRightColor": "rgba(255, 255, 255, 1)",
    "borderBottomWidth": 1,
    "borderBottomColor": "rgba(255, 255, 255, 1)",
    "borderLeftWidth": 1,
    "borderLeftColor": "rgba(255, 255, 255, 1)",
    "borderTopLeftRadius": 2.67,
    "borderTopRightRadius": 2.67,
    "borderBottomLeftRadius": 2.67,
    "borderBottomRightRadius": 2.67,
    "width": 22,
    "height": 11.33,
    "left": 0,
    "top": 0
  },
  "about_statusBar_battery_cap": {
    "opacity": 0.4000000059604645,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 3.33,
    "height": 6,
    "left": 22,
    "top": 2.67
  },
  "about_statusBar_battery_capacity": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 1)",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "borderTopWidth": 1,
    "borderTopColor": "rgba(0, 0, 0, 0)",
    "borderRightWidth": 1,
    "borderRightColor": "rgba(0, 0, 0, 0)",
    "borderBottomWidth": 1,
    "borderBottomColor": "rgba(0, 0, 0, 0)",
    "borderLeftWidth": 1,
    "borderLeftColor": "rgba(0, 0, 0, 0)",
    "borderTopLeftRadius": 1.33,
    "borderTopRightRadius": 1.33,
    "borderBottomLeftRadius": 1.33,
    "borderBottomRightRadius": 1.33,
    "width": 17,
    "height": 6.33,
    "left": 1.5,
    "top": 1.5
  },
  "about_statusBar_wifi": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 17.33,
    "height": 13,
    "left": 294,
    "top": 2.33
  },
  "about_statusBar_cellularConnection": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 19,
    "height": 12.67,
    "left": 272,
    "top": 2.67
  },
  "about_statusBar_timeStyle": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 54,
    "height": 18,
    "left": 0,
    "top": 0
  },
  "about_statusBar_timeStyle_time": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(255, 255, 255, 1)",
    "fontSize": 15,
    "fontWeight": "700",
    "fontStyle": "normal",
    "fontFamily": "SF Pro Text",
    "textAlign": "center",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 54,
    "height": 18,
    "left": 0,
    "top": 0
  },
  "about_x02smile": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 171.21,
    "height": 160.5,
    "left": 102.5,
    "top": 43.5
  },
  "about_zeroTwo": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(0, 0, 0, 1)",
    "fontSize": 31,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 131,
    "height": 36,
    "left": 126,
    "top": 198
  },
  "about_apeSpecialOps": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(0, 0, 0, 1)",
    "fontSize": 17,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 126,
    "height": 20,
    "left": 62,
    "top": 239
  },
  "about_parasite": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(0, 0, 0, 1)",
    "fontSize": 17,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 60,
    "height": 20,
    "left": 207,
    "top": 239
  },
  "about_line1": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 2,
    "height": 16,
    "left": 196.5,
    "top": 243.5
  },
  "about_profileb0253c68": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(0, 0, 0, 1)",
    "fontSize": 30,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 88,
    "height": 35,
    "left": 38.5,
    "top": 259
  },
  "about_aboutb40aa9f5": {
    "opacity": 0.800000011920929,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(255, 255, 255, 1)",
    "fontSize": 30,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 82,
    "height": 35,
    "left": 257,
    "top": 259
  },
  "about_line2": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 187,
    "height": 5,
    "left": 188.5,
    "top": 292
  },
  "about_rectangle2": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(216, 33, 33, 1)",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "borderTopLeftRadius": 0,
    "borderTopRightRadius": 0,
    "borderBottomLeftRadius": 0,
    "borderBottomRightRadius": 0,
    "shadowColor": "rgb(0,  0,  0)",
    "shadowOpacity": 0.6,
    "shadowOffset": {
      "width": 0,
      "height": 1
    },
    "shadowRadius": 10,
    "width": 375,
    "height": 54,
    "left": 0,
    "top": 295
  },
  "about_follow": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(255, 255, 255, 1)",
    "fontSize": 36,
    "fontWeight": "400",
    "fontStyle": "normal",
    "fontFamily": "Rockwell",
    "textAlign": "center",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 110,
    "height": 42,
    "left": 132.5,
    "top": 299.5
  },
  "about_group4": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 300,
    "height": 168,
    "left": 38,
    "top": 508
  },
  "about_group4_zeroTwoFeature": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "borderTopLeftRadius": 0,
    "borderTopRightRadius": 0,
    "borderBottomLeftRadius": 0,
    "borderBottomRightRadius": 0,
    "width": 300,
    "height": 168,
    "left": 0,
    "top": 0
  },
  "about_group4_polygon1": {
    "opacity": 0.8299999833106995,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "shadowColor": "rgb(0,  0,  0)",
    "shadowOpacity": 0.7294117647058823,
    "shadowOffset": {
      "width": 0,
      "height": 3
    },
    "shadowRadius": 6,
    "width": 75,
    "height": 65,
    "left": 111.49,
    "top": 39.76
  },
  "about_group5": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 139,
    "height": 22,
    "left": 38,
    "top": 486
  },
  "about_group5_rectangle78dcec7cc": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "borderTopLeftRadius": 0,
    "borderTopRightRadius": 0,
    "borderBottomLeftRadius": 0,
    "borderBottomRightRadius": 0,
    "width": 139,
    "height": 22,
    "left": 0,
    "top": 0
  },
  "about_group5_featuredVideo": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(255, 255, 255, 1)",
    "fontSize": 19,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 132,
    "height": 22,
    "left": 3,
    "top": 0
  },
  "about_group6": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 92,
    "height": 24,
    "left": 38,
    "top": 356
  },
  "about_group6_rectangle7e0b0b399": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "borderTopLeftRadius": 0,
    "borderTopRightRadius": 0,
    "borderBottomLeftRadius": 0,
    "borderBottomRightRadius": 0,
    "width": 92,
    "height": 24,
    "left": 0,
    "top": 0
  },
  "about_group6_following": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(255, 255, 255, 1)",
    "fontSize": 19,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 84,
    "height": 22,
    "left": 3,
    "top": 0
  },
  "about_repeatGrid2": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 436,
    "height": 71,
    "left": 44,
    "top": 389
  },
  "about_repeatGrid2_repeatGrid254d0e28822bd": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 55,
    "height": 71,
    "left": 0,
    "top": 0
  },
  "about_repeatGrid2_repeatGrid254d0e28822bd_goro": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 55,
    "height": 55,
    "left": 0,
    "top": 0
  },
  "about_repeatGrid2_repeatGrid254d0e28822bd_characters": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(255, 255, 255, 1)",
    "fontSize": 11,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 25,
    "height": 13,
    "left": 12,
    "top": 58
  },
  "about_repeatGrid2_repeatGrid20fd38bc26e24": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 55,
    "height": 71,
    "left": 75,
    "top": 0
  },
  "about_repeatGrid2_repeatGrid20fd38bc26e24_hiro91e722e3": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 55,
    "height": 55,
    "left": 0,
    "top": 0
  },
  "about_repeatGrid2_repeatGrid20fd38bc26e24_ichigob080c1ed": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(255, 255, 255, 1)",
    "fontSize": 11,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 21,
    "height": 13,
    "left": 12,
    "top": 58
  },
  "about_repeatGrid2_repeatGrid244eb61dd0fd4": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 55,
    "height": 71,
    "left": 150,
    "top": 0
  },
  "about_repeatGrid2_repeatGrid244eb61dd0fd4_hiroaa575910": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 55,
    "height": 55,
    "left": 0,
    "top": 0
  },
  "about_repeatGrid2_repeatGrid244eb61dd0fd4_ichigod68334a6": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(255, 255, 255, 1)",
    "fontSize": 11,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 31,
    "height": 13,
    "left": 12,
    "top": 58
  },
  "about_repeatGrid2_repeatGrid2159e3899a1f1": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 55,
    "height": 71,
    "left": 225,
    "top": 0
  },
  "about_repeatGrid2_repeatGrid2159e3899a1f1_hiro56a49510": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 55,
    "height": 55,
    "left": 0,
    "top": 0
  },
  "about_repeatGrid2_repeatGrid2159e3899a1f1_ichigo5914f51a": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(255, 255, 255, 1)",
    "fontSize": 11,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 27,
    "height": 13,
    "left": 12,
    "top": 58
  },
  "about_repeatGrid2_repeatGrid2138e6e86d200": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 55,
    "height": 71,
    "left": 300,
    "top": 0
  },
  "about_repeatGrid2_repeatGrid2138e6e86d200_hiro95307941": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 55,
    "height": 55,
    "left": 0,
    "top": 0
  },
  "about_repeatGrid2_repeatGrid2138e6e86d200_ichigo57d965be": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(255, 255, 255, 1)",
    "fontSize": 11,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 24,
    "height": 13,
    "left": 12,
    "top": 58
  },
  "about_repeatGrid2_repeatGrid2Eef815140c8c": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 55,
    "height": 71,
    "left": 375,
    "top": 0
  },
  "about_repeatGrid2_repeatGrid2Eef815140c8c_hiro": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 55,
    "height": 55,
    "left": 0,
    "top": 0
  },
  "about_repeatGrid2_repeatGrid2Eef815140c8c_ichigo": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(255, 255, 255, 1)",
    "fontSize": 11,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 38,
    "height": 13,
    "left": 12,
    "top": 58
  },
  "about_group7": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 111,
    "height": 26,
    "left": 38,
    "top": 699
  },
  "about_group7_rectangle7": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "borderTopLeftRadius": 0,
    "borderTopRightRadius": 0,
    "borderBottomLeftRadius": 0,
    "borderBottomRightRadius": 0,
    "width": 111,
    "height": 26,
    "left": 0,
    "top": 0
  },
  "about_group7_background0d9e790e": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(255, 255, 255, 1)",
    "fontSize": 19,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 103,
    "height": 22,
    "left": 3,
    "top": 0
  },
  "about_talkAboutYourselfInThisSectionTalkAboutYourLifeAndhowYouGotIntroducedIntoThisPlatformAndHowYouAreaGodNow": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "color": "rgba(255, 255, 255, 1)",
    "fontSize": 12,
    "fontWeight": "400",
    "fontStyle": "italic",
    "fontFamily": "Rockwell",
    "textAlign": "left",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 312,
    "height": 42,
    "left": 38,
    "top": 728
  },
  "about_barsToolbarIphoneCompactDark3Glyphs": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 375,
    "height": 83,
    "left": 0,
    "top": 756
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_background5f27efc2": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 375,
    "height": 83,
    "left": 0,
    "top": 0
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_background5f27efc2_background": {
    "opacity": 0.9985939860343933,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "borderTopLeftRadius": 0,
    "borderTopRightRadius": 0,
    "borderBottomLeftRadius": 0,
    "borderBottomRightRadius": 0,
    "width": 375,
    "height": 83,
    "left": 0,
    "top": 0
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_profile": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 44,
    "height": 44,
    "left": 306,
    "top": 3
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_profile_framee4e32c60": {
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 1)",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "borderTopLeftRadius": 0,
    "borderTopRightRadius": 0,
    "borderBottomLeftRadius": 0,
    "borderBottomRightRadius": 0,
    "width": 44,
    "height": 44,
    "left": 0,
    "top": 0
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_profile_group3": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 39,
    "height": 44,
    "left": 3,
    "top": 0
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_profile_group3_ellipse3": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 25,
    "height": 24,
    "left": 7,
    "top": 0
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_profile_group3_rectangle5": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(0, 0, 0, 1)",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "borderTopLeftRadius": 8,
    "borderTopRightRadius": 8,
    "borderBottomLeftRadius": 8,
    "borderBottomRightRadius": 8,
    "width": 39,
    "height": 18,
    "left": 0,
    "top": 26
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_profile_group3_rectangle6": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(0, 0, 0, 1)",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "borderTopLeftRadius": 0,
    "borderTopRightRadius": 0,
    "borderBottomLeftRadius": 0,
    "borderBottomRightRadius": 0,
    "width": 39,
    "height": 14,
    "left": 0,
    "top": 30
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_add": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 44,
    "height": 44,
    "left": 166,
    "top": 3
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_add_frame036c7384": {
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 1)",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "borderTopLeftRadius": 0,
    "borderTopRightRadius": 0,
    "borderBottomLeftRadius": 0,
    "borderBottomRightRadius": 0,
    "width": 44,
    "height": 44,
    "left": 0,
    "top": 0
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_add_group1": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 41,
    "height": 42,
    "left": 1,
    "top": 2
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_add_group1_rectangle3": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "rgba(255, 255, 255, 0)",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "borderTopWidth": 3,
    "borderTopColor": "rgba(0, 0, 0, 1)",
    "borderRightWidth": 3,
    "borderRightColor": "rgba(0, 0, 0, 1)",
    "borderBottomWidth": 3,
    "borderBottomColor": "rgba(0, 0, 0, 1)",
    "borderLeftWidth": 3,
    "borderLeftColor": "rgba(0, 0, 0, 1)",
    "borderTopLeftRadius": 8,
    "borderTopRightRadius": 8,
    "borderBottomLeftRadius": 8,
    "borderBottomRightRadius": 8,
    "width": 41,
    "height": 42,
    "left": 0,
    "top": 0
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_add_group1_line3": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 40.28,
    "height": 3,
    "left": 0.36,
    "top": 19
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_add_group1_line4": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 3,
    "height": 41,
    "left": 19,
    "top": 0.36
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_home": {
    "opacity": 1,
    "position": "absolute",
    "backgroundColor": "transparent",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "paddingTop": 0,
    "paddingRight": 0,
    "paddingBottom": 0,
    "paddingLeft": 0,
    "width": 44,
    "height": 44,
    "left": 26,
    "top": 3
  },
  "about_barsToolbarIphoneCompactDark3Glyphs_home_frame": {
    "opacity": 1,
    "position": "absolute",
    "marginTop": 0,
    "marginRight": 0,
    "marginBottom": 0,
    "marginLeft": 0,
    "borderTopLeftRadius": 0,
    "borderTopRightRadius": 0,
    "borderBottomLeftRadius": 0,
    "borderBottomRightRadius": 0,
    "width": 44,
    "height": 44,
    "left": 0,
    "top": 0
  }
});